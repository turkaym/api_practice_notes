from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.note import NotesCreate, NotesUpdate, NotesOut
from app.services import notes as note_service

router = APIRouter(
    prefix="/notes",
    tags=["notes"]
)


@router.post("/", response_model=NotesOut, status_code=status.HTTP_201_CREATED)
def create_note(note: NotesCreate, db: Session = Depends(get_db)):
    return note_service.create_note(db, note)


@router.get("/", response_model=list[NotesOut])
def get_notes(db: Session = Depends(get_db)):
    return note_service.get_notes(db)


@router.get("{note_id}", response_model=NotesOut)
def get_note_by_id(note_id: int, db: Session = Depends(get_db)):
    return note_service.get_notes_by_id(db, note_id)


@router.put("{note_id}", response_model=NotesOut)
def update_note(note_id: int, note_update: NotesUpdate, db: Session = Depends(get_db)):
    return note_service.update_note(db, note_id, note_update)


@router.delete("{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    return note_service.delete_note(db, note_id)
