# 🧠 NLP Desktop App (Tkinter + Hugging Face Transformers)

A simple yet powerful **NLP Desktop Application** built using **Python Tkinter** and **Hugging Face Transformers**.  
It lets users perform:
- 🗣️ **Sentiment Analysis**
- 🏷️ **Named Entity Recognition (NER)**
- 😃 **Emotion Detection**
- 🔐 **User Registration & Login** (stored in local JSON database)

---

## 🧩 Features
- Clean GUI built with **Tkinter**
- Local JSON-based database (`db.json`) for users  
- **Pre-trained Hugging Face models** for NLP tasks  
- Modular structure (`main.py`, `myapi.py`, `mydb.py`)  
- Beginner-friendly and fully commented code

---

## 🧠 Models Used

| Task | Model | Source |
|------|--------|--------|
| Sentiment Analysis | `distilbert-base-uncased-finetuned-sst-2-english` | Hugging Face |
| Named Entity Recognition | `dslim/bert-base-NER` | Hugging Face |
| Emotion Detection | `j-hartmann/emotion-english-distilroberta-base` | Hugging Face |

---

## ⚙️ Requirements

### 🐍 Python Version
```
Python 3.8 or above
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install transformers torch
```

> 💡 Note: `tkinter` comes pre-installed with most Python versions.

---

## 🧩 Project Structure
```
NLP-App/
│
├── main.py          # GUI (Login, Register, Home, Analysis)
├── mydb.py          # Handles JSON-based database
├── myapi.py         # Contains NLP pipeline logic (Transformers)
├── db.json          # Local database file
└── Resources/
    └── icon.ico     # App icon
```

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/nlp-app.git
   cd nlp-app
   ```

2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

---

## 🧠 How It Works
- The app loads pre-trained **Hugging Face models** locally using `transformers` and `torch`.
- On first run, the models are automatically downloaded.
- User data (name, email, password) is stored in `db.json`.
- GUI built using **Tkinter** handles login, registration, and navigation between NLP tools.
  
---

## 🤝 Contributing
Pull requests are welcome!  
If you have ideas for improvement, feel free to fork and submit a PR.

---

## 🧑‍💻 Author
 **GitHub -> BRZxx001**  
🔗 [GitHub Profile](https://github.com/BRZxx001)  
💬 “Making NLP accessible through simple GUIs.”

---

⭐ **If you like this project, give it a star on GitHub!**
