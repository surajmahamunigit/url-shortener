from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.routes import auth, links, redirect
from app.db.init_db import init_db


# Replaces the deprecated @app.on_event("startup") from older FastAPI versions
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(auth.router)
app.include_router(links.router)
app.include_router(redirect.router)


@app.get("/")
def root():
    return {"message": "URL Shortener API is running"}
