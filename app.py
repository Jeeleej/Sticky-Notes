from flask import Flask, render_template, request, redirect, url_for
import markdown

app = Flask(__name__)

notes = {}
note_id = 1

@app.route("/")
def home():
    query = request.args.get("q", "")
    filtered_notes = {i: n for i, n in notes.items() if query.lower() in n["title"].lower() or query.lower() in n["content"].lower()}
    return render_template("index.html", notes=filtered_notes, query=query)

@app.route("/note/<int:id>")
def view_note(id):
    note = notes.get(id)
    if not note:
        return "Note not found!", 404
    html_content = markdown.markdown(note["content"])
    return render_template("view_note.html", note=note, id=id, html_content=html_content)

@app.route("/add", methods=["GET", "POST"])
def add_note():
    global note_id
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        notes[note_id] = {"title": title, "content": content}
        note_id += 1
        return redirect(url_for("home"))
    return render_template("edit_note.html", action="Add")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_note(id):
    note = notes.get(id)
    if not note:
        return "Note not found!", 404

    if request.method == "POST":
        note["title"] = request.form["title"]
        note["content"] = request.form["content"]
        return redirect(url_for("view_note", id=id))
    return render_template("edit_note.html", action="Edit", note=note)

@app.route("/delete/<int:id>", methods=["POST"])
def delete_note(id):
    if id in notes:
        notes.pop(id)
    return redirect(url_for("home"))
    
if __name__ == "__main__":
    app.run(debug=True)
