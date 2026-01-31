from fastapi import FastAPI
from app.api import notes, users, auth
from app.db.database import engine
from app.db import models
from app.core.config import settings

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

app.include_router(notes.router)
app.include_router(users.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {
        "app": settings.APP_NAME,
        "environment": settings.ENV,
        "status": "running"
    }
