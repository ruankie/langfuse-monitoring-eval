---
marp: true
theme: default
class: invert
# size: 16:9
footer: Ruan Pretorius | October 2024 | ![grayscale height:15](../assets/melio-logo.svg)
style: |
  section {
    font-size: 32px;
  }
---

![bg left:35% height:300px](../assets/pyconza.png)

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

![height:50](../assets/melio-logo.svg)

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

## ⚡ Setting Up

> Local LLMs for zero-cost learning and prototyping

### 🦙 Ollama

- For locally running LLMs
- Available for macOS, Linux, and Windows (preview)
- Familiar Docker feel with `:version` tags and commands like `pull` and `run`

![bg right:30% height:250px](../assets/ollama.png)

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
  
![bg right:30% height:250px](../assets/ollama.png)

---

## 🧰 Monitoring LLM Apps with Langfuse

- **What is Langfuse?** 🚀
  - Open-source platform for LLM tracing and evaluation
  - Focus on detailed app performance metrics 📊
- **Why Monitor?**
  - Spot issues before they impact users 🔍
  - Ensure consistent LLM performance 📈
---

## 🏗️ Setting Up Langfuse

- **Installing Langfuse** 🛠️
  - Installation guide
  - Integrating Langfuse with Python SDK 🐍
- **Configuring Langfuse for Tracing**
  - Key configurations for monitoring and logs 📝
  - Setting up evaluation datasets 📚
---

## 🎯 Monitoring with Langfuse: Live Example

- **Using Langfuse's Python Decorator** 🔄
  - Tracing requests and responses in LLM apps
  - Real-time dashboard view 📊
- **Example Implementation**:
  - Simple Langfuse integration in a Python LLM app
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

  ![height:50](../assets/melio-logo.svg)