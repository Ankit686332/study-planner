# 🧠 Study Architect AI 

**Study Architect AI** is a professional-grade, full-stack Generative AI application that serves as a personalized academic consultant. It eliminates "information overload" by transforming broad learning goals into structured, time-bound, and level-appropriate roadmaps.

Developed by **Ankit Mohanty**.

---

## 🚀 Key Features
- **Personalized Planning:** Tailors roadmaps based on user expertise (Beginner, Intermediate, or Advanced).
- **Time-Adaptive Logic:** Adjusts the intensity of the curriculum based on the user's weekly availability.
- **Modern Web Interface:** A clean, branded UI built with Streamlit and custom CSS.
- **Exportable Data:** Users can download their generated study plans as `.txt` files for offline reference.
- **Secure Architecture:** Implements `.env` management to protect sensitive API credentials from exposure.

---

## 🛠️ Technical Stack
- **Language:** Python 3.10+
- **Frontend:** [Streamlit](https://streamlit.io/) (Data-centric UI Framework)
- **AI Engine:** [Google Gemini 2.5 Flash-Lite](https://ai.google.dev/) (LLM for logical inference)
- **Environment Management:** `python-dotenv`
- **Styling:** Custom CSS Injection

---

## 📂 Project Structure
```text
AI_Study_Planner/
├── .env                # API Keys (Excluded from Git for security)
├── requirements.txt    # Required Python libraries
├── app.py              # Main logic, UI, and AI Integration
└── README.md           # Project documentation
