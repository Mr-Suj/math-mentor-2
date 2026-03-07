# 🧠 AI Math Mentor
### Multimodal AI System for Solving Mathematical Problems

AI Math Mentor is an **AI-powered system that solves mathematics problems from text, images, or audio using a multi-agent architecture, Retrieval-Augmented Generation (RAG), and symbolic verification.**

The system mimics how a human tutor solves problems:

```
Understand → Retrieve Knowledge → Reason → Solve → Verify → Explain
```

---

# 🚀 Key Features

## 🧩 Multimodal Input
Users can submit problems in multiple formats:

- ✍️ Text-based math questions  
- 🖼 Image-based problems (OCR extraction)  
- 🎙 Spoken questions (Speech‑to‑Text)

---

## 🧠 Multi‑Agent Reasoning System

The system uses specialized agents:

| Agent | Role |
|------|------|
| **Parser Agent** | Understands and structures the math problem |
| **Retriever Agent** | Searches relevant mathematical knowledge |
| **Solver Agent** | Computes symbolic or numeric solution |
| **Explanation Agent** | Generates step‑by‑step reasoning |
| **Verification Agent** | Validates solution correctness |

This architecture **reduces hallucinations and improves reliability.**

---

## 📚 Retrieval Augmented Generation (RAG)

Instead of relying only on the LLM, the system retrieves relevant mathematical knowledge.

Components:

- **BGE embeddings** for semantic search  
- **ChromaDB** vector database  
- Custom **math knowledge base**

This enables **context‑aware reasoning.**

---

## 🔢 Symbolic Math Verification

Mathematical correctness is ensured using **SymPy**.

Example:

```
Input:
Find derivative of x² + 3x

Output:
2x + 3
```

The symbolic engine verifies the result mathematically.

---

## 🎙 Multimodal Processing

| Input | Technology |
|------|------|
| Images | PaddleOCR |
| Audio | Whisper Speech‑to‑Text |
| Text | Gemini LLM |

---

## 🧑‍🏫 Human‑in‑the‑Loop (HITL)

If a solution is incorrect:

- Users can correct it
- System stores feedback
- Improves future responses

---

# 🏗 System Architecture

```
                ┌────────────────────┐
                │      User Input     │
                │  Text / Image / Audio │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │  Multimodal Layer   │
                │ OCR / Speech‑to‑Text│
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │   Problem Parser    │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │  RAG Retrieval      │
                │ ChromaDB + BGE      │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │  Multi‑Agent Solver │
                │ Planning + Reasoning│
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Symbolic Verification │
                │      (SymPy)         │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Step‑by‑Step Explanation │
                └──────────┬─────────┘
                           │
                           ▼
                ┌────────────────────┐
                │      Frontend UI     │
                │      Streamlit       │
                └────────────────────┘
```

---

# ⚙️ Tech Stack

### 🤖 AI / LLM
- Gemini 1.5 Pro

### 📚 Retrieval
- BGE-small-en embeddings
- ChromaDB vector database

### 🔢 Math Engine
- SymPy
- NumPy

### 🎙 Multimodal Processing
- PaddleOCR
- OpenAI Whisper

### 🌐 Backend
- FastAPI

### 💻 Frontend
- Streamlit

### ☁ Deployment
- HuggingFace Spaces

---

# 📂 Project Structure

```
math-mentor
│
├── app
│   ├── agents
│   ├── api
│   ├── multimodal
│   ├── rag
│   ├── solver
│   └── verifier
│
├── frontend
│   └── app.py
│
├── tests
│
├── knowledgebase
│
├── requirements.txt
├── packages.txt
├── app.py
└── README.md
```

---

# 🖥 Running the Project Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start backend

```bash
uvicorn app.api.main:app --reload
```

### Start frontend

```bash
streamlit run frontend/app.py
```

---

# 📊 Example Workflow

Example input:

```
Find derivative of x² + 3x
```

System pipeline:

```
1️⃣ Parse math expression
2️⃣ Retrieve relevant calculus rules
3️⃣ Symbolically differentiate
4️⃣ Verify result using SymPy
5️⃣ Generate explanation
```

Output:

```
Derivative = 2x + 3
```

with full step‑by‑step explanation.

---

# 🎯 Why This Project Matters

This project demonstrates **real AI engineering skills**:

- Multimodal AI systems
- Retrieval‑Augmented Generation
- Multi‑agent architectures
- Symbolic reasoning integration
- Full‑stack AI deployment

---

# 👨‍💻 Author

Built as an **AI Engineering system design project demonstrating advanced applied AI engineering.**

---

# ⭐ Future Improvements

- Mathematical diagram understanding
- Step verification with theorem libraries
- Adaptive tutoring feedback
- Reinforcement learning from user corrections

---

# 📸 Demo

(Add HuggingFace deployment link here after deployment)

---

⭐ If you found this interesting, give the repo a star!