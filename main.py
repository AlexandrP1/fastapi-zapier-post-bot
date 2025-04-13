from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class TopicRequest(BaseModel):
    topic: str

@app.post("/generate-post")
async def generate_post(data: TopicRequest):
    prompt = f"Напиши пост для Telegram-блога на тему: {data.topic}. Структура: заголовок, краткий подзаголовок, основной текст. Используй неформальный тон и реальные примеры."

    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Ты опытный копирайтер, создающий посты для Telegram-блога."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return {"post": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}