from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models import Note
from app.schemas.note import NotesCreate, NotesUpdate


def create_note(db: Session, note: NotesCreate):
    new_note = Note(
        title=note.title,
        content=note.content
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


def get_notes(db: Session):
    return db.query(Note).all()


def get_notes_by_id(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="note not found")
    else:
        return note


def update_note(db: Session, note_id: int, note_update: NotesUpdate):
    note = get_notes_by_id(db, note_id)
    note.title = note_update.title
    note.content = note_update.content
    db.commit()
    db.refresh(note)
    return note


def delete_note(db: Session, note_id: int):
    note = get_notes_by_id(db, note_id)
    db.delete(note)
    db.commit()
