import hashlib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Req(BaseModel):
    text: str

@app.post("/")
async def process(req: Req):
    text = req.text
    uppercase = text.upper()
    char_count = len(text.replace('-', '').replace(' ', ''))
    word_count = len(text.replace('-', ' ').split())
    sha = hashlib.sha256(text.encode()).hexdigest()[:16]
    verify = hashlib.sha256(
        f"upper:{uppercase}:chars:{char_count}:words:{word_count}".encode()
    ).hexdigest()[:12]
    return {
        "uppercase": uppercase,
        "char_count": char_count,
        "word_count": word_count,
        "sha256": sha,
        "verify": verify
    }
