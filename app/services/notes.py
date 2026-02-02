from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db.models import Note, User
from app.schemas.note import NoteCreate, NoteUpdate


def create_note(db: Session, note: NoteCreate, user: User):
    new_note = Note(
        title=note.title,
        content=note.content,
        user_id=user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


def get_notes(db: Session, user: User, limit: int = 10, offset: int = 0):
    return db.query(Note).filter(Note.user_id == user.id).order_by(Note.created_at.desc()).limit(limit).offset(offset).all()


def get_note_by_id(db: Session, note_id: int, user: User):
    note = db.query(Note).filter(Note.id == note_id,
                                 Note.user_id == user.id).first()

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return note


def update_note(db: Session, note_id: int, note_update: NoteUpdate, user: User):
    note = get_note_by_id(db, note_id, user)
    note.title = note_update.title
    note.content = note_update.content
    db.commit()
    db.refresh(note)
    return note


def delete_note(db: Session, note_id: int, user: User):
    note = get_note_by_id(db, note_id, user)
    db.delete(note)
    db.commit()
