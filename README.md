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
- **Pre-trained Hugging Face models** for all NLP tasks  
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
pip install transformers torch pillow
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
   git clone https://github.com/<your-username>/nlp-desktop-app.git
   cd nlp-desktop-app
   ```

2. (Optional) Create virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate   # Mac/Linux
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
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

## 💡 Future Improvements
- Add text summarization or translation  
- Add speech-to-text / text-to-speech  
- Switch JSON DB → SQLite  
- Add light/dark themes  

---

## 🤝 Contributing
Pull requests are welcome!  
If you have ideas for improvement, feel free to fork and submit a PR.

---

## 🧑‍💻 Author
**[Your Name or GitHub Username]**  
🔗 [GitHub Profile](https://github.com/<your-username>)  
💬 “Making NLP accessible through simple GUIs.”

---

## 🪪 License
This project is licensed under the **MIT License**.

---

⭐ **If you like this project, give it a star on GitHub!**
