from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


notes = []
next_id = 1


@app.route("/")
def home():
    return {"message": "CI/CD is working "}


@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)   #Check this return type ASAP


@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    for note in notes:
        if note["id"] == note_id:
            return jsonify(note)
    return {"error": "Not found"}, 404


@app.route("/notes", methods=["POST"])
def create_note():
    global next_id

    data = request.json

    note = {
        "id": next_id,
        "title": data["title"],
        "content": data["content"],
        "created_at": datetime.now().isoformat() 
    }

    notes.append(note)
    next_id += 1

    return jsonify(note), 201


@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.json

    for note in notes:
        if note["id"] == note_id:
            note["title"] = data["title"]
            note["content"] = data["content"]
            return jsonify(note)

    return {"error": "Not found"}, 404


@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n["id"] != note_id]
    return {"message": "Deleted"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    