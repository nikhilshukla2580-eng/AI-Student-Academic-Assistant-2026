# 🎓 APSU Student Academic AI Assistant

An interactive, multi-tiered AI-based academic assistant designed for students and faculty of **Awadhesh Pratap Singh University (APSU), Rewa**.

---

## ✨ Features

- **University Portal Direct Integration**: Direct access to MPOnline Portal, Marksheet Portal, and Official APSU Website.
- **Student Chat Interface**: Voice input (Speech-to-Text) and text queries for examination, fee payment, and syllabus queries.
- **Teacher Admin Dashboard**: Dedicated admin panel (`frontend/admin.html`) allowing faculty to publish live notices and FAQs.
- **Smart Response System**: Keyword matching and dynamic fallback routing for APSU services.

---

## 📁 Repository Structure

├── backend/
│   ├── app.py          # Flask API handling chatbot & admin endpoints
│   └── chatbot.py      # Core response logic & data management
├── data/
│   └── faq.json        # APSU FAQs, notices, and official link database
└── frontend/
├── index.html      # Student Chatbot UI (Voice + Links)
├── admin.html      # Teacher / Admin Dashboard
├── script.js       # Voice Recognition & API calls
└── style.css       # Styling for Chat UI & Admin Panel

---

## 🚀 Quick Start (Local Setup)

1. **Install Dependencies**:
   ```bash
   pip install flask flask-cors

   cd backend
python app.py
