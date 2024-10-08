import sys

sys.path.append("../agent")
from agents import BasicAgent, AdvancedAgent

from asyncio import run
import logging
from dotenv import load_dotenv
import argparse
from langfuse import Langfuse
from typing import Tuple
from tqdm import tqdm
from ragas.metrics import (
    # faithfulness,
    # context_precision,
    context_recall,
    answer_correctness,
)
from ragas.run_config import RunConfig
from ragas.metrics.base import MetricWithLLM, MetricWithEmbeddings
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
# from langchain_ollama.chat_models import ChatOllama
# from langchain_ollama.llms import OllamaLLM

# Config
EVAL_EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EVAL_LLM_NAME = "llama3" # "llama3.1:8b"
METRICS = [answer_correctness, context_recall]


def invoke_agent(prompt: str, agent_version: str) -> Tuple[str, str, list[str]]:
    """
    Invokes the specified agent with a given prompt and returns its response.

    Args:
        prompt (str): The input prompt to be processed by the agent.
        agent_version (str): The version of the agent to be invoked.

    Returns:
        Tuple containing:
            - final_response (str): The final response generated by the agent.
            - lf_trace_id (str): The trace ID associated with Langfuse for tracking.
            - docs (list[str]): A list of documents retrieved by the agent during the invocation.
    """
    if agent_version == "0.0.1":
        agent = BasicAgent()
    else:
        agent = AdvancedAgent()

    # Invoke agent
    response = agent.invoke(prompt)

    # Deconstruct response
    final_response = response["final_response"]
    lf_trace_id = response["lf_trace_id"]
    docs = response.get("docs", "")

    return final_response, lf_trace_id, docs


def init_ragas_metrics(metrics, llm, embedding) -> None:
    """Initialise Ragas metrics with the relevant LLM and embedding model."""
    for metric in metrics:
        if isinstance(metric, MetricWithLLM):
            metric.llm = llm
        if isinstance(metric, MetricWithEmbeddings):
            metric.embeddings = embedding
        run_config = RunConfig()
        metric.init(run_config)


async def score_with_ragas(
    query: str, chunks: list[str], answer: str, ground_truth: str
) -> dict[str, float]:
    """
    Get Ragas scores for a given user question with its generated answer and retrieved documents.

    Args:
        query (str): The user question that was asked to the agent.
        chunks (list[str]): A list of retrieved documents from the vector store
            to support answering the user question.
        answer (str): The agent's generated answer.
        ground_truth (str): The expected answer.

        Returns:
            dict[str, float]: A dictionary of calculated metrics with metric names as keys.
    """
    scores = {}
    for m in METRICS:
        print(f"calculating {m.name}")
        scores[m.name] = await m.ascore(
            row={
                "question": query,
                "contexts": chunks,
                "answer": answer,
                "ground_truth": ground_truth,
            }
        )
    return scores


def run_eval(agent_version: str, dataset_name: str) -> None:
    """
    Run evaluation of a specific agent version on a given dataset.

    Args:
        agent_version (str): The version of the agent to evaluate.
        dataset_name (str): The name of the dataset to evaluate against.
    """
    # Langfuse variables
    langfuse_run_name = f"Chatbot v{agent_version}"
    langfuse_run_desc = f"Eval agent v{agent_version} on {dataset_name}"
    langfuse_run_meta = {
        "agent_version": agent_version,
        "eval_llm": EVAL_LLM_NAME,
        "eval_embedding_model": EVAL_EMBEDDING_MODEL,
    }

    # Initialise eval llm and embedding model
    eval_llm = ChatOllama(model=EVAL_LLM_NAME, temperature=0)
    eval_embedding = HuggingFaceEmbeddings(model_name=EVAL_EMBEDDING_MODEL)

    # Initialise Langfuse client
    load_dotenv()
    langfuse = Langfuse()

    dataset = langfuse.get_dataset(dataset_name)

    init_ragas_metrics(
        metrics=METRICS,
        llm=LangchainLLMWrapper(eval_llm),
        embedding=LangchainEmbeddingsWrapper(eval_embedding),
    )

    # Loop through dataset items
    for item in tqdm(dataset.items):
        try:
            # Invoke agent
            output, lf_trace_id, docs_list = invoke_agent(
                prompt=item.input, agent_version=agent_version
            )

            # Link dataset run item to trace
            item.link(
                trace_or_observation=None,
                run_name=langfuse_run_name,
                run_description=langfuse_run_desc,
                run_metadata=langfuse_run_meta,
                trace_id=lf_trace_id,
            )

            # Get evaluation metrics dict
            scores: dict[str, float] = run(
                score_with_ragas(
                    query=item.input,
                    chunks=docs_list,
                    answer=output,
                    ground_truth=item.expected_output,
                )
            )

            # Add scores to trace
            for s in scores:
                langfuse.score(
                    trace_id=lf_trace_id,
                    name=s,
                    value=scores[s],
                    # comment="This is a comment",  # optional, useful to add reasoning
                )

        except Exception as ex:
            print(f"Continuing to next item. Error: {ex}")


if __name__ == "__main__":
    """
    Run agent evaluation.

    Example usage:
        ```shell
        # Example eval of agent 0.0.1 on eval_data_v1 dataset
        python run_eval.py --dataset_name eval-dataset-v1 --agent_ver 0.0.1
        ```

    Args:
        --dataset_name (str): Name of the dataset to evaluate.
        --agent_interface_ver (str): Version of the agent interface lambda to evaluate.
    """
    # Set up logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Parse input args to specify dataset and agent version
    parser = argparse.ArgumentParser(description="Evaluate agent performance.")
    parser.add_argument(
        "--dataset_name",
        type=str,
        required=True,
        help="Name of the dataset to evaluate.",
    )
    parser.add_argument(
        "--agent_ver",
        type=str,
        required=True,
        help="Version of the agent to evaluate.",
    )

    args = parser.parse_args()
    run_eval(dataset_name=args.dataset_name, agent_version=args.agent_ver)
