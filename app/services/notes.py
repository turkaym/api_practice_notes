from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models import Note
from app.schemas.note import NoteCreate, NoteUpdate


def create_note(db: Session, note: NoteCreate):
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


def get_note_by_id(db: Session, note_id: int):
    note = db.query(Note).filter(Note.id == note_id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return note


def update_note(db: Session, note_id: int, note_update: NoteUpdate):
    note = get_note_by_id(db, note_id)
    note.title = note_update.title
    note.content = note_update.content
    db.commit()
    db.refresh(note)
    return note


def delete_note(db: Session, note_id: int):
    note = get_note_by_id(db, note_id)
    db.delete(note)
    db.commit()
