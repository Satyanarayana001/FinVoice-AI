# FinVoice-AI  
### Offline Voice-Based Financial Assistant

FinVoice-AI is a **voice-enabled financial assistant** that answers **banking and finance questions** using an **offline, LLM-style reasoning engine**.  
It works without OpenAI or cloud APIs and focuses on **low latency, privacy, and zero cost**.

---

## Key Features

- Voice input using Speech-to-Text (Whisper)
- Offline LLM-style reasoning (no external APIs)
- Context-aware conversations
- Finance and banking domain focused
- Text-to-Speech voice responses
- Low latency and privacy-friendly

---

## Questions It Can Answer

### Banking & Finance
- What is EMI?
- How is EMI calculated?
- What is loan interest?
- What is a bank transaction?
- What does debit or credit mean?
- What is account balance?

### Financial Math
- EMI formula explanation
- Simple vs compound interest
- Annual to monthly interest conversion
- Loan tenure vs EMI impact
- Balance calculation after transactions

---

## Project Structure
FinVoice-AI/
├── app.py               # FastAPI entry point
├── stt.py               # Speech-to-text logic
├── tts.py               # Text-to-speech logic
├── llm.py               # Response generation (offline logic)
├── intent_router.py     # Intent classification
├── context_manager.py   # Conversation handling
├── prompts.py           # Response templates
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
└── demo.mp4             # Demo video

---

## ⚙️ How It Works

1. User speaks a finance-related question
2. Audio is converted to text (Speech-to-Text)
3. Intent is detected (EMI, Interest, Transaction, etc.)
4. Conversation context is maintained
5. Offline LLM-style logic generates a response
6. Response is converted back to voice (Text-to-Speech)

---

## 🧠 LLM-Style Reasoning (Offline)

FinVoice-AI uses:
- Semantic keyword scoring
- Intent-based reasoning
- Context-aware responses
- Intelligent fallbacks and follow-ups

This design reduces **cost, latency, and dependency on cloud APIs** while remaining explainable and efficient.

---

## 🛠 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Satyanarayana/FinVoice-AI.git
cd FinVoice-AI
---

### 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

###3️⃣ Install Dependencies
pip install -r requirements.txt

###4️⃣ Run Application
python -m uvicorn app:app --reload

###5️⃣ Open API Docs
http://127.0.0.1:8000/docs