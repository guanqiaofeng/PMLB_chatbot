# 🤖 Labguru Chatbot

A command-line assistant to query structured data from [**Labguru**](https://www.labguru.com/), using a combination of **LLM-based natural language parsing** and structured data retrieval.

## 🔍 What It Does

This chatbot allows users to:

- Count or list **cases**, **specimens**, **organoids**, **xenografts**, **assays**, and various **omics** data (WES, WGS, RNA-seq, ATAC, etc.)
- Use natural language queries like:
  - `how many specimens`
  - `list organoids starting with CSC`
  - `how many WES`
  - `list patients that name starts with BPTO`
- Parse queries using **LLaMA 3** for intent and filter extraction, then execute structured lookups via Python backend.

## 🛠️ Project Structure

```bash
.
├── chatbot/
│   ├── __init__.py
│   ├── labguru_api.py       # Core functions to retrieve structured Labguru data
│   ├── nlu_llm.py           # LLM-based intent + filter parsing (via LLaMA3)
├── interface/
│   ├── cli.py               # CLI interface for the chatbot
├── pixi.toml                # Pixi environment and dependencies
├── README.md                # You’re here
```

## 🚀 How to Run

1. Install Pixi (if not already)
   
   See: https://prefix.dev/docs/pixi/

2. Run the chatbot
```
pixi run chat
```
   
3. Try some example prompts:
```
how many specimens
list organoids name starts with CSC
list patients that name contains PHLC
```

## 🧠 Powered By

- LLaMA3 — for lightweight intent parsing
- Structured retrieval — deterministic querying of structured Labguru metadata
- Pixi — reproducible Python environment

## 📦 Dependencies

All dependencies are managed via pixi.toml. Notable one include:
- python-dotenv (database API configuration)

## 🧪 Example Intent JSON

A typical parsed LLM response looks like:
```
{
  "intent": "list_organoids",
  "filters": {
    "organoids_name_startswith": "CSC"
  }
}
```

## ✅ Features

- ✅ Count and list commands for structured entities
- ✅ Case-insensitive and typo-tolerant alias resolution (organlids → organoids)
- ✅ Natural language understanding using LLMs
- ✅ CLI interface for offline use

## 🔮 Roadmap

- integrate Q & A base LLM agent
- integrate Knowledge graph based LLM agent
- Add RAG-based querying for unstructured text (path reports, notes)
- Web UI
- Authentication and multi-user support

## 👤 Author

Guanqiao Feng

## 📄 License

MIT License
