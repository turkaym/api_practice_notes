from pydantic import BaseModel


class NotesCreate(BaseModel):
    title: str
    content: str


class NotesUpdate(BaseModel):
    title: str
    content: str


class NotesOut(BaseModel):
    id: int
    title: str
    content: str
