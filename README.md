# Monitoring and evaluating LLM apps with Langfuse.

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

1. Set up infrastructure

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

1. Run the example apps and see the traces logged in Langfuse

    - Simple examples in `./simple_examples/`
    - Or some more complex examples in `./agent/`
