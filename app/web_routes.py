from flask import Blueprint, redirect, render_template, request, url_for

from .models import Note, db

web_bp = Blueprint("web", __name__)


def _validate_form(form):
    required_fields = ("title", "content", "course")
    missing = [field for field in required_fields if not form.get(field, "").strip()]
    if missing:
        return f"Please fill in: {', '.join(missing)}."
    return None


@web_bp.get("/")
def home():
    notes = Note.query.order_by(Note.updated_at.desc()).all()
    return render_template("index.html", notes=notes, form_data={}, edit_note=None, error=None)


@web_bp.post("/notes/create")
def create_note_page():
    error = _validate_form(request.form)
    if error:
        notes = Note.query.order_by(Note.updated_at.desc()).all()
        return render_template(
            "index.html",
            notes=notes,
            form_data=request.form,
            edit_note=None,
            error=error,
        ), 400

    note = Note(
        title=request.form["title"].strip(),
        content=request.form["content"].strip(),
        course=request.form["course"].strip(),
    )
    db.session.add(note)
    db.session.commit()
    return redirect(url_for("web.home"))


@web_bp.get("/notes/<int:note_id>/edit")
def edit_note_page(note_id):
    note = db.session.get(Note, note_id)
    if note is None:
        return redirect(url_for("web.home"))

    notes = Note.query.order_by(Note.updated_at.desc()).all()
    return render_template(
        "index.html",
        notes=notes,
        form_data=note.to_dict(),
        edit_note=note,
        error=None,
    )


@web_bp.post("/notes/<int:note_id>/edit")
def update_note_page(note_id):
    note = db.session.get(Note, note_id)
    if note is None:
        return redirect(url_for("web.home"))

    error = _validate_form(request.form)
    if error:
        notes = Note.query.order_by(Note.updated_at.desc()).all()
        return render_template(
            "index.html",
            notes=notes,
            form_data=request.form,
            edit_note=note,
            error=error,
        ), 400

    note.title = request.form["title"].strip()
    note.content = request.form["content"].strip()
    note.course = request.form["course"].strip()
    db.session.commit()
    return redirect(url_for("web.home"))


@web_bp.post("/notes/<int:note_id>/delete")
def delete_note_page(note_id):
    note = db.session.get(Note, note_id)
    if note is not None:
        db.session.delete(note)
        db.session.commit()
    return redirect(url_for("web.home"))
