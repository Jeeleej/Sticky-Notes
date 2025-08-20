# Sticky-Notes

A simple **note-taking web application** built with **Flask**.  
It allows users to **create, edit, delete, and search notes**, with support for writing in **Markdown** and rendering into **HTML**.  

---

## 🚀 Features
- ✍️ Create and edit notes in Markdown  
- 🖋 Render notes as clean HTML  
- 🔍 Search notes by title 
- 🗑️ Delete notes with confirmation  
- 🎨 Minimal, responsive UI  

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, Jinja2 templates  
- **Library:** `markdown` (for rendering)  

---

## 📂 Project Structure
```text
flask-notes-app/
│── app.py # Main Flask app
│── templates/
│ ├── base.html # Base layout
│ ├── index.html # Homepage (list + search notes)
│ ├── view_note.html # View a single note
│ ├── edit_note.html # Add/Edit note
```
---

## ▶️ Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-notes-app.git
   cd flask-notes-app
   ```
2. Install dependencies:
   ```bash
   pip install flask markdown
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open in browser:
   👉 http://127.0.0.1:5000

