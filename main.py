from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API


class NLP_APP:
    def __init__(self):
        # --- INITIAL SETUP ---
        self.dbo = Database()
        self.apio = API()

        # Create main window
        self.root = Tk()
        self.root.title("NLP App")
        self.root.iconbitmap("Resources/icon.ico")
        self.root.geometry("350x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#607D8B")

        # Load login page first
        self.login_gui()
        self.root.mainloop()

    # ==========================================================
    # --- LOGIN GUI ---
    # ==========================================================
    def login_gui(self):
        self.clear()

        # Heading
        heading = Label(self.root, text='NLP App', bg="#607D8B", fg="#f5f5f5")
        heading.pack(pady=(30, 30))
        heading.configure(font=("Verdana", 24, "bold"))

        # Email input
        Label(self.root, text='Enter Your Email').pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 10), ipady=4)

        # Password input
        Label(self.root, text='Enter Your Password').pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        # Login button
        Button(self.root, text='Login!', width=25, height=2,
               command=self.perform_login).pack(pady=(20, 10))

        # Redirect to register
        Label(self.root, text='Not a Member?').pack(pady=(20, 10))
        Button(self.root, text='Register Now!', command=self.register_gui).pack(pady=(10, 10))

    # ==========================================================
    # --- REGISTER GUI ---
    # ==========================================================
    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg="#607D8B", fg="#f5f5f5")
        heading.pack(pady=(30, 30))
        heading.configure(font=("Verdana", 24, "bold"))

        # Name input
        Label(self.root, text='Enter Your Name').pack(pady=(10, 10))
        self.name_input = Entry(self.root, width=40)
        self.name_input.pack(pady=(5, 10), ipady=4)

        # Email input
        Label(self.root, text='Enter Your Email').pack(pady=(10, 10))
        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 10), ipady=4)

        # Password input
        Label(self.root, text='Enter Your Password').pack(pady=(10, 10))
        self.password_input = Entry(self.root, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        # Register button
        Button(self.root, text='Register!', width=25, height=2,
               command=self.perform_registration).pack(pady=(20, 10))

        # Redirect to login
        Label(self.root, text='Already a Member?').pack(pady=(20, 10))
        Button(self.root, text='Login Now!', command=self.login_gui).pack(pady=(10, 10))

    # ==========================================================
    # --- COMMON: CLEAR SCREEN ---
    # ==========================================================
    def clear(self):
        # Destroy all current widgets
        for i in self.root.pack_slaves():
            i.destroy()

    # ==========================================================
    # --- REGISTRATION LOGIC ---
    # ==========================================================
    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)

        if response:
            messagebox.showinfo('Success', 'Registration Successful. You can Login Now')
            self.name_input.delete(0, END)
            self.email_input.delete(0, END)
            self.password_input.delete(0, END)
        else:
            messagebox.showerror('Error', 'Email Already Exists')

    # ==========================================================
    # --- LOGIN LOGIC ---
    # ==========================================================
    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo('Success', 'Login Successful')
            self.email_input.delete(0, END)
            self.password_input.delete(0, END)
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect Email/Password')

    # ==========================================================
    # --- HOME SCREEN ---
    # ==========================================================
    def home_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg="#607D8B", fg="#f5f5f5")
        heading.pack(pady=(30, 30))
        heading.configure(font=("Verdana", 24, "bold"))

        Button(self.root, text='Sentiment Analysis', width=30, height=4,
               command=self.sentiment_gui).pack(pady=(20, 10))
        Button(self.root, text='Named Entity Recognition', width=30, height=4,
               command=self.ner_gui).pack(pady=(20, 10))
        Button(self.root, text='Emotion Analysis', width=30, height=4,
               command=self.emotion_gui).pack(pady=(20, 10))

        Button(self.root, text='Logout', command=self.login_gui).pack(pady=(10, 10))

    # ==========================================================
    # --- SENTIMENT GUI ---
    # ==========================================================
    def sentiment_gui(self):
        self.clear()

        Label(self.root, text='NLP App', bg="#607D8B", fg="#f5f5f5",
              font=("Verdana", 24, "bold")).pack(pady=(30, 20))
        Label(self.root, text='Sentiment Analysis', bg="#607D8B", fg="#f5f5f5",
              font=("Verdana", 24)).pack(pady=(10, 10))

        Label(self.root, text='Enter The Text').pack(pady=(10, 10))
        self.sentiment_input = Entry(self.root, width=40)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        Button(self.root, text='Analyse', command=self.do_sentiment_analysis).pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='#607D8B', fg='white', font=('verdana', 16))
        self.sentiment_result.pack(pady=(10, 10))

        Button(self.root, text='Go Back', command=self.home_gui).pack(pady=(10, 10))

    # ==========================================================
    # --- NER GUI ---
    # ==========================================================
    def ner_gui(self):
        self.clear()

        Label(self.root, text='NLP App', bg="#607D8B", fg="#f5f5f5",
              font=("Verdana", 24, "bold")).pack(pady=(30, 20))
        Label(self.root, text='Named Entity Recognition', bg="#607D8B", fg="#f5f5f5",
              font=("Verdana", 18)).pack(pady=(10, 10))

        Label(self.root, text='Enter Text').pack(pady=(10, 10))
        self.ner_input = Entry(self.root, width=40)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        Button(self.root, text='Analyze', command=self.do_ner_analysis).pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#607D8B', fg='white', font=('verdana', 12))
        self.ner_result.pack(pady=(10, 10))

        Button(self.root, text='Go Back', command=self.home_gui).pack(pady=(10, 10))

    # ==========================================================
    # --- EMOTION GUI ---
    # ==========================================================
    def emotion_gui(self):
        self.clear()

        Label(self.root, text='NLP App', bg="#607D8B", fg="#f5f5f5",
              font=("Verdana", 24, "bold")).pack(pady=(30, 20))
        Label(self.root, text='Emotion Analysis', bg="#607D8B", fg="#f5f5f5",
              font=("Verdana", 20)).pack(pady=(10, 10))

        Label(self.root, text='Enter Text').pack(pady=(10, 10))
        self.emotion_input = Entry(self.root, width=40)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        Button(self.root, text='Analyze', command=self.do_emotion_analysis).pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='#607D8B', fg='white', font=('verdana', 12))
        self.emotion_result.pack(pady=(10, 10))

        Button(self.root, text='Go Back', command=self.home_gui).pack(pady=(10, 10))

    # ==========================================================
    # --- SENTIMENT LOGIC ---
    # ==========================================================
    def do_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        for i in result:
            for j in i:
                if j == 'label':
                    label = i[j]
                elif j == 'score':
                    score = i[j]

        self.sentiment_result['text'] = f"{label} -> {score:.4f}"

    # ==========================================================
    # --- NER LOGIC ---
    # ==========================================================
    def do_ner_analysis(self):
        text = self.ner_input.get()
        result = self.apio.named_entity_recognition(text)

        if not result:
            self.ner_result['text'] = "No result"
            return

        merged = []
        current = None

        # Merge subword tokens
        for ent in result:
            word = ent['word'].replace("##", "")
            if current and ent['entity_group'] == current['entity_group'] and ent['start'] == current['end']:
                current['word'] += word
                current['end'] = ent['end']
                current['score'] = max(current['score'], ent['score'])
            else:
                if current:
                    merged.append(current)
                current = ent.copy()
                current['word'] = word
        if current:
            merged.append(current)

        # Merge consecutive same entities
        final = []
        i = 0
        while i < len(merged):
            curr = merged[i]
            while (
                i + 1 < len(merged)
                and merged[i + 1]['entity_group'] == curr['entity_group']
                and merged[i + 1]['start'] == curr['end'] + 1
            ):
                curr['word'] += " " + merged[i + 1]['word']
                curr['end'] = merged[i + 1]['end']
                curr['score'] = max(curr['score'], merged[i + 1]['score'])
                i += 1
            final.append(curr)
            i += 1

        # Format output
        res = ""
        for i in final:
            res += f"{i['word']} -> {i['entity_group']} ({i['score']:.4f})\n"

        self.ner_result['text'] = res.strip()

    # ==========================================================
    # --- EMOTION LOGIC ---
    # ==========================================================
    def do_emotion_analysis(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)

        if not result or not result[0]:
            self.emotion_result['text'] = "No result"
            return

        emotions = [(i['label'], i['score']) for i in result[0]]
        emotions = sorted(emotions, key=lambda x: x[1], reverse=True)[:3]

        res_line = ""
        for e in emotions:
            res_line += f"{e[0]} -> {e[1]:.4f}\n"

        self.emotion_result['text'] = res_line.strip()


# ==========================================================
# --- APP START ---
# ==========================================================
nlp = NLP_APP()
