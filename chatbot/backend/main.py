from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai

openai.api_key ="your-api-key-here"
app = FastAPI()

# allow your HTML to talk to python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": message.text}]
    )

    # FIX: extract text properly
    reply = response.choices[0].message.content

    return {"reply": reply}

