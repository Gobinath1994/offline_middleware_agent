
# 🧾 Offline CRM Agent

A full-stack GenAI middleware application that allows users to ask natural language questions about CRM/ERP data — such as invoices, overdue payments, and customer status — all processed offline using a local LLM (via LM Studio or Ollama).

---

## 🚀 Features

- 💬 Natural Language Query → SQL → MySQL
- 🤖 Offline LLM via LM Studio (Mistral, TinyLLaMA, etc.)
- 🧠 LangChain agent + Tool calling
- 📡 FastAPI backend
- 🖥️ Streamlit frontend
- 🗃️ MySQL for CRM data (invoices, customers)

---

## 🧱 Project Structure

```
offline_middleware_agent/
├── AegisAI/                  # Python virtual environment (created via venv)
├── frontend/
│   └── app.py                # Streamlit UI for user queries
├── tools/
│   └── crm_tools.py          # Tool functions for agent (e.g., get_overdue_invoices)
├── db/
│   └── db_utils.py           # MySQL database connection helper
├── langchain_agent.py        # LangChain agent setup and tool registration
├── main.py                   # FastAPI backend to process incoming queries
└── README.md                 # You’re here!
```

---

## ⚙️ Setup Instructions

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/your-username/offline_middleware_agent.git
cd offline_middleware_agent
```

### ✅ 2. Create Virtual Environment

```bash
python3 -m venv AegisAI
source AegisAI/bin/activate
```

### ✅ 3. Install Requirements

```bash
pip install -r requirements.txt
```

> Make sure you’ve also installed **MySQL**, **Streamlit**, and **LM Studio** separately.

---

## 🧠 Prerequisites

- ✅ Python 3.11+
- ✅ MySQL installed and running
- ✅ LM Studio (or Ollama) running at `http://localhost:1234/v1`
- ✅ A local model loaded (e.g., Mistral-7B)

---

## 🗄️ MySQL Setup

Create a database and table:

```sql
CREATE DATABASE crm_db;

USE crm_db;

CREATE TABLE invoices (
  id INT PRIMARY KEY AUTO_INCREMENT,
  customer_name VARCHAR(255),
  amount DECIMAL(10, 2),
  due_date DATE,
  status VARCHAR(50)
);

-- Insert sample data
INSERT INTO invoices (customer_name, amount, due_date, status)
VALUES 
  ('Polaris Central', 1200.00, '2025-04-01', 'overdue'),
  ('Bobcat Forklifts', 800.00, '2025-04-15', 'paid');
```

---

## 🧪 How to Run the Project

### 🔌 Start LM Studio (with a model like `Mistral`)

### 🖥️ 1. Start the FastAPI backend

```bash
uvicorn main:app --reload
```

It will run at `http://localhost:8000`

### 🧾 2. Start the Streamlit frontend

```bash
streamlit run frontend/app.py
```

It will run at `http://localhost:8501`

---

## ✨ Example Query

> 💬 _“Show overdue invoices for Polaris Central”_

The agent uses the LLM to:
- Parse intent
- Choose `get_overdue_invoices()`
- Run a SQL query
- Return the result formatted cleanly

---

## 🔐 Optional Enhancements

- ✅ Add user auth (OAuth or token)
- ✅ Display invoice tables in the UI
- ✅ Export results to PDF or CSV
- ✅ Add more tools like `get_total_due`, `get_customer_balance`

---

## 📄 License

MIT License.  
Feel free to use and modify for internal or personal CRM/ERP automation.

---

## 👨‍💻 Author

**Gobinath Sindhuja**  
Built with ❤️ using LangChain + LM Studio
