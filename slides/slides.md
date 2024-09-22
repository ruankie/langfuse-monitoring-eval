---
marp: true
theme: default
class: invert
# size: 16:9
footer: Ruan Pretorius | October 2024 | ![grayscale height:15](../assets/logos/melio-logo.svg)
style: |
  section {
    font-size: 32px;
  }
---

![bg left:35% height:300px](../assets/logos/pyconza.png)

# Monitoring and Evaluating LLM Apps
> *Using Langfuse*

---

## About me

##### Hi there, I'm Ruan Pretorius 👋

- ☕ I turn coffee into AI
- 🖥 I am a data scientist at *[melio.ai](https://melio.ai/)*
  - We help you build and deploy your data intensive apps to unlock value from your data, follow us on LinkedIn
- 🔗 You can find me on GitHub *[@ruankie](https://github.com/ruankie)*
- ✉️ Or contact me via email: *ruan@melio.ai*

#

![height:50](../assets/logos/melio-logo.svg)

---

## 🚏 Outline

- **Introduction**: Why monitor/evaluate LLM apps?
- **Setup**: Local LLMs for prototyping
- **Monitoring**: with Langfuse
- **Evaluation**: LLM-assisted with Ollama and Langfuse
- **Takeaways and Conclusion**

---

## ❓ Why Monitor & Evaluate LLM Apps?

- **Ensure Quality & Performance**
  - Track hallucination, retrieval accuracy, latency, etc.
  - To maintain a high-quality user experience
- **Detect Errors**
  - Harmful outputs
- **Identify Areas of Improvement**
  - Reduce costs
  - Reduce latency
  - Improve answers
  - If failure occurs, see when and where

---

## 🏗️ What We'll Be Building

![bg right height:600px](../assets/architecture/arch-dark.png)

---

## ⚡ Setting Up

> Local LLMs for zero-cost learning and prototyping

### 🦙 Ollama

- For locally running LLMs
- Available for macOS, Linux, and Windows (preview)
- Familiar Docker feel with `:version` tags and commands like `pull` and `run`

![bg right:30% height:200px](../assets/logos/ollama.png)

---

## 🦙 Ollama Setup

- ⬇️ Download app from [`https://ollama.com/`](https://ollama.com/)
- Download LLM of choice

  ```shell
  ollama pull llama3.1:8b
  ```

- To test, run LLM in terminal

  ```shell
  ollama run llama3.1:8b
  ```

![bg right:30% height:200px](../assets/logos/ollama.png)

---

TODO: Show gif of Ollama running in terminal

---

## 📊 Monitoring LLM Apps with Langfuse

- **What is Langfuse?**
  - Open Source LLM engineering platform
  - For tracing, evaluation, prompt management, etc.
  - Can be used to debug and improve your LLM apps
  - Can use as service or self-host

![bg right:30% height:150px](../assets/logos/langfuse.png)

---

## 🏗️ Setting Up Langfuse

> Option 1: Use as service

- Sign up at [`https://cloud.langfuse.com/`](https://cloud.langfuse.com/)
- Select region for hosting (`EU` or `US`)
- Create a new Project
- Generate API keys for sending traces

![bg right:30% height:150px](../assets/logos/langfuse.png)

---

## 🏗️ Setting Up Langfuse

> Option 2: Locally, with Docker compose

- Requires `docker` and `docker compose` - get with [Docker Desktop](https://docs.docker.com/get-started/get-docker/)
- Run Docker compose to spin up local Langfuse

  ```shell
  # Clone the Langfuse repository
  git clone https://github.com/langfuse/langfuse.git
  cd langfuse
  
  # Start the server and database
  docker compose up
  ```

---

## 🏗️ Setting Up Langfuse

> Before using in code

- Finally, pip-install the package to use it

  ```shell
  pip install langfuse
  ```

---

## ✅ Done Setting Up Langfuse

- Now we have our infrastructure set up
  - Langfuse server with web UI (at `localhost:3000`)
  - Postgres DB as backend (at `localhost:5432`)
- And the Python package needed to communicate with it

---

TODO: Show gif of Langfuse dashboard

---

## 🎯 Monitoring with Langfuse

> Instrumenting your code

- Configure your app to talk to your Langfuse instance
  - Python decorator
  - LangChain callback handler

---

## 📡 Langfuse Instrumentation

> Python decorator

- Configure your app to talk to your Langfuse instance
  - Python decorator
  - LangChain callback handler

---






## 📊 LLM-Assisted Evaluation with Langfuse

- **Evaluation Datasets** 📚
  - How Langfuse helps score and evaluate your LLM outputs
- **LLM-Assisted Scoring** 🎯
  - Automated evaluation using predefined metrics
  - Feedback loop to improve LLM performance
---

## 📈 Best Practices for Monitoring and Evaluation

- **Key Takeaways** 💡
  - Prototyping fast and free with local LLMs 🖥️
  - Monitoring with Langfuse to ensure app robustness 📊
  - LLM-assisted evaluation for continuous improvement 🔁
---

## 🎉 Conclusion: Elevate Your LLM Workflow

- **Summary** of key points:
  - Local LLM setup with Ollama 🚀
  - Langfuse for monitoring and evaluation 🧰
  - Automating scoring and feedback 📝
- **Final Thoughts**: Start small, scale smart! 🌟
---

#

## <!--fit--> 🐍 Thank you!

#

- 🔗 GitHub: *[@ruankie](https://github.com/ruankie)*
- ✉️ Email: *ruan@melio.ai*
- 🏠 Melio website: *[melio.ai](https://melio.ai)*

  ![height:50](../assets/logos/melio-logo.svg)