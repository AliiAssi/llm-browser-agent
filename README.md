# 🔍 LLM Browser Agent Prototype

A lightweight prototype that combines a high-speed LLaMA-4 model hosted on Groq with a web-enabled autonomous agent powered by [`browser-use`](https://github.com/chadwhitacre/browser-use). This system simulates a browsing assistant that can research topics in real time and return coherent, grounded answers.

---

## ⚙️ Features

- 🧠 Powered by [Meta LLaMA-4 Maverick 17B 128E](https://groq.com)
- 🌐 Agent uses synthetic browsing to research and synthesize information
- ⚡ Supports asynchronous execution via Python's `asyncio`
- 🧪 Clean prototype setup – ready for expansion

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AliiAssi/llm-browser-agent.git
cd llm-browser-agent
```

### 2. Install Requirements
Make sure you have Python 3.8 or later installed.

```bash
pip install browser-use steel-sdk
```

### 3. Run the Prototype

```bash
python main.py
```

---

## 🧪 Prototype Status

This is an **experimental prototype** to test the integration of real-time LLM querying with autonomous browsing. It is not production-ready but provides a strong starting point for future tools, agents, and search-based assistants.

---

## 📋 Sample Output

```bash
> tell me about KamKalima

KamKalima is a digital Arabic language learning platform designed to support educators and students...
```

---

## 🔧 Technologies Used

* 🧠 `ChatGroq` from `browser_use.llm`
* 🌐 `Agent` class for simulated web tasks
* 🌀 `asyncio` for asynchronous control flow
* 🧰 Optional: `steel-sdk` for extended tool support

---

## 👤 Author

**Ali Assi**  
[LinkedIn](https://linkedin.com/in/aliassii) · [GitHub](https://github.com/AliiAssi)

---

## 💡 Inspiration

This project explores the idea of *autonomous LLM agents* that use search capabilities to complete real-world research tasks. Inspired by the possibilities of integrating LLMs with modular agent toolkits and Groq's high-throughput inference.