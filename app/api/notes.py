from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.note import NoteCreate, NoteUpdate, NoteOut
from app.services import notes as note_service
from app.core.security import get_current_user
from app.db.models import User


router = APIRouter(
    prefix="/notes",
    tags=["notes"]
)


@router.post("/", response_model=NoteOut, status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return note_service.create_note(db, note, current_user)


@router.get("/", response_model=list[NoteOut])
def get_notes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user), limit: int = Query(10, ge=1, le=100), offset: int = Query(0, ge=0)):
    return note_service.get_notes(db, current_user, limit, offset)


@router.get("/{note_id}", response_model=NoteOut)
def get_note_by_id(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return note_service.get_note_by_id(db, note_id, current_user)


@router.put("/{note_id}", response_model=NoteOut)
def update_note(note_id: int, note_update: NoteUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return note_service.update_note(db, note_id, note_update, current_user)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note_service.delete_note(db, note_id, current_user)
