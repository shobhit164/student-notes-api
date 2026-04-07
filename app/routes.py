from flask import Blueprint, jsonify, request

from .models import Note, db

notes_bp = Blueprint("notes", __name__)


def _validate_payload(payload):
    if not payload:
        return "Request body must be valid JSON."

    required_fields = ("title", "content", "course")
    missing = [field for field in required_fields if not payload.get(field)]
    if missing:
        return f"Missing required fields: {', '.join(missing)}."

    return None


@notes_bp.get("")
def list_notes():
    notes = Note.query.order_by(Note.updated_at.desc()).all()
    return jsonify([note.to_dict() for note in notes]), 200


@notes_bp.get("/<int:note_id>")
def get_note(note_id):
    note = db.session.get(Note, note_id)
    if note is None:
        return jsonify({"error": f"Note with id {note_id} not found."}), 404
    return jsonify(note.to_dict()), 200


@notes_bp.post("")
def create_note():
    payload = request.get_json(silent=True)
    validation_error = _validate_payload(payload)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    note = Note(
        title=payload["title"].strip(),
        content=payload["content"].strip(),
        course=payload["course"].strip(),
    )
    db.session.add(note)
    db.session.commit()

    return jsonify(note.to_dict()), 201


@notes_bp.put("/<int:note_id>")
def update_note(note_id):
    note = db.session.get(Note, note_id)
    if note is None:
        return jsonify({"error": f"Note with id {note_id} not found."}), 404

    payload = request.get_json(silent=True)
    validation_error = _validate_payload(payload)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    note.title = payload["title"].strip()
    note.content = payload["content"].strip()
    note.course = payload["course"].strip()
    db.session.commit()

    return jsonify(note.to_dict()), 200


@notes_bp.delete("/<int:note_id>")
def delete_note(note_id):
    note = db.session.get(Note, note_id)
    if note is None:
        return jsonify({"error": f"Note with id {note_id} not found."}), 404

    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": f"Note with id {note_id} deleted successfully."}), 200
