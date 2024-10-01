# Monitoring and evaluating LLM apps with Langfuse

> Presented at PyConZA 2024.

## Overview

In the rapidly evolving landscape of AI, the ability to quickly iterate on prototypes and ensure robust performance of apps built around language models is crucial for developers and data scientists. This talk focuses on leveraging free and open-source tools to build, monitor, and evaluate LLM applications, providing a cost-effective approach to rapid development and deployment within the Python ecosystem.

**Topics Covered:**

- Setting up local LLMs for fast prototyping (7 min):
  - Using Ollama for easy setup and deployment on local machines.
  - Running LLMs locally to build and test prototypes without incurring costs.
- Monitoring LLM apps with Langfuse (15 min):
  - Introduction to Langfuse, an open-source LLM engineering platform.
  - Configuring Langfuse for tracing and evaluation.
  - Implementing Langfuse's Python decorator and SDK for detailed monitoring.
- LLM-assisted evaluation (7 min):
  - Using Langfuse to set up evaluation datasets and scoring responses of your LLM app.

**Target Audience and Takeaways:**

This talk is aimed at developers and data scientists who are interested in monitoring and optimising their LLM applications. By the end of the session, attendees will have a better understanding of how to set up and monitor their LLM apps using Langfuse, as well as how to leverage local LLMs for rapid prototyping and evaluation. They will walk away with actionable insights and practical knowledge to enhance their workflows, making their AI solutions more efficient and reliable.

## Usage

1. Set up local Langfuse infrastructure

    ```shell
    cd langfuse
    docker compose up
    ```

1. Open the Langfuse UI and create a project

    1. Go to `http://localhost:3000/`
    1. Create an account and log in (if done locally, this only stores a user account in your local database)
    1. Create a new project and call it `pycon-demo`

1. Set up virtual env to run code in (and install dependencies)

    ```shell
    python -m venv .venv && source .venv/bin/activate
    pip install -r requirements.txt
    ```

1. Configure Langfuse by setting environment variables. Create a `.env` file and populate it with your Langfuse details (see `.env.example` for an example).

1. Create a local knowledge base that your apps can use to retrieve information from.

    > This only needs to be done once. You don't need to do this to run the `simple_examples`.

    ```shell
    cd knowledge_base
    ./gen_kb.sh
    ```

1. Monitoring: Run the example apps and see the traces logged in Langfuse

    - Simple examples in `./simple_examples/`
    - Or some more complex examples in `./agent/`

1. Eval: Create an eval dataset and run eval on both agent versions

    > Run all these commands from the `eval/` directory

    - Create the eval dataset in Langfuse

      ```shell
      python create_dataset.py
      ```

    - Run eval on a version of the agent (e.g. `0.0.1`)

      ```shell
      python run_eval.py --dataset_name eval-dataset-v1 --agent_ver 0.0.1
      ```

1. Inspect all Traces,Datasets, and Dataset Runs in the Langfuse Dashboard (at `http://localhost:3000/`)

## References

- https://langfuse.com/docs
- https://langfuse.com/guides/cookbook/datasets
- https://langfuse.com/guides/cookbook/evaluation_of_rag_with_ragas
- https://ollama.com/
- https://python.langchain.com/docs
- https://applied-llms.org/#evaluation-monitoring
- https://www.anthropic.com/news/evaluating-ai-systems
