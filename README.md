# Sticky-Notes

A simple **Flask-based web application** for managing personal notes with authentication and environment-based configuration using `.flaskenv`.

---

## 🚀 Features
- 🔐 User authentication (Sign Up, Login, Logout)
- 📝 Create, edit, delete, and view notes
- ⚙️ Environment variable configuration via `.flaskenv`
- 💾 SQLite database integration
- 🎨 Responsive UI with Bootstrap

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Other Tools:** python-dotenv, Flask-WTF

---

## 📂 Project Structure
```text
flask-notes-app/
│── app.py
│── requirements.txt
│── .flaskenv.example
│── templates/
│ ├── base.html
│ ├── index.html
│ └── login.html
│── static/
│ └── style.css
```

---

## ⚡ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-notes-app.git
   cd flask-notes-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.flaskenv` file:
   ```bash
   FLASK_APP=app.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   ```
4. Run the app:
   ```bash
   flask run
   ```
5. Open in browser:
  👉 http://127.0.0.1:5000/
