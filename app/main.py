
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.avatar import get_introduction_audio

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="Cartoon AI Avatar",
    description="An AI avatar that introduces itself with voice",
    version="1.0.0",
)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "templates" / "index.html")


@app.get("/api/introduction")
def introduction():
    try:
        text, audio_url = get_introduction_audio()

        return {
            "message": text,
            "audio_url": audio_url,
        }
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="Unable to generate audio. Check your internet connection.",
        )


@app.get("/health")
def health():
    return {"status": "healthy"}
