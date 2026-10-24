
from pathlib import Path
from gtts import gTTS

BASE_DIR = Path(__file__).resolve().parent
AUDIO_DIR = BASE_DIR / "static" / "audio"
AUDIO_FILE = AUDIO_DIR / "introduction.mp3"

INTRODUCTION = (
    "Hi! Welcome to my application. "
    "I am your virtual AI assistant. "
    "I can help you with information, answer your questions, "
    "and guide you through the features of this application. "
    "Let's get started!"
)


def get_introduction_audio():
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    if not AUDIO_FILE.exists():
        tts = gTTS(
            text=INTRODUCTION,
            lang="en",
            slow=False
        )
        tts.save(str(AUDIO_FILE))

    return INTRODUCTION, "/static/audio/introduction.mp3"
