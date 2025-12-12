# ⚡ AI Chatbot - Dark Modern Web UI

A **powerful AI chatbot** with a sleek **dark-themed frontend** and a **Python FastAPI backend**.  
Chat with GPT-powered AI directly from your browser! 🖤✨

---

## 🌟 Features

- 🖤 Modern **dark UI** with smooth animations  
- 📱 Fully **responsive design** (mobile + desktop)  
- 🤖 Powered by **OpenAI GPT-4o-mini**  
- 💻 Frontend built with **HTML / CSS / JavaScript**  
- 🐍 Backend built with **Python + FastAPI**  
- 🔒 Safe API handling using **`.env` file**  
- ⚡ Easy to extend (voice, files, custom datasets)

---

## 🛠️ Technologies Used

| Layer       | Technology / Library |
|------------|--------------------|
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Python, FastAPI, Pydantic, python-dotenv |
| API        | OpenAI GPT API |
| Server     | Uvicorn ASGI server |
| Others     | CORS for frontend-backend communication |

---

## 📂 Project Structure

```
chatbot/
├── backend/
│     ├── main.py        # FastAPI backend
      ├── requirements.txt
│     └── .env           # Stores your OpenAI API key (do NOT upload)
└── frontend/
      └── index.html     # Chatbot frontend
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Ajuu1801/AI-Chatbot---Dark-Modern-Web-UI.git
cd AI-Chatbot---Dark-Modern-Web-UI
```

### 2️⃣ Setup Backend

```bash
cd backend
python -m venv venv       # optional but recommended
pip install -r requirements.txt
```

### 3️⃣ Add OpenAI API Key

Create a `.env` file in the `backend/` folder:

```
OPENAI_API_KEY=your_openai_api_key_here
```

⚠️ **Do NOT upload `.env` to GitHub!**

### 4️⃣ Run Backend Server

```bash
uvicorn main:app --reload
```

Your backend will be running at:

```
http://127.0.0.1:8000
```

### 5️⃣ Open Frontend

Open `frontend/index.html` in your browser.  
Type a message → see the AI respond! 💬✨

---

## 🔧 How It Works

1. Frontend (HTML/JS) sends your message via **POST** request to `/chat`.  
2. FastAPI backend receives it, forwards to **OpenAI GPT API**.  
3. OpenAI returns a response → backend sends it back.  
4. Frontend shows the message in **animated chat bubbles**.

---

## 🛡️ Safety Notes

- Keep your OpenAI API key **private** 🔑  
- Use `.env` for sensitive keys  
- Never commit `.env` to GitHub

---

## ✨ Future Improvements

- 🎤 Voice input / speech recognition  
- 🔊 Bot voice replies (text-to-speech)  
- 📄 Upload PDF/DOCX → ask questions from files  
- 🧠 Train on custom datasets  
- 🌐 Deploy to the web

---

## 📝 License

Open-source project. Feel free to **fork, modify, and use**.

---

## 👨‍💻 Author

**Ajay Gawas** – [Portfolio](https://portfolliox1.netlify.app/)  
