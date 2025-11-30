import os
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import AsyncIterable, Iterable
from openai import Stream
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionChunk
from .models.qwen_flash import QwenFlash


class Item(BaseModel):
    messages: Iterable[ChatCompletionMessageParam]


qwen_flash = QwenFlash(os.environ["DASHSCOPE_API_KEY"])


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)


async def stream_generator(
    stream: Stream[ChatCompletionChunk],
) -> AsyncIterable[str]:
    for chunk in stream:
        yield chunk.choices[0].delta.content or ""


@app.post("/api/chat/response")
async def root(item: Item):
    response = qwen_flash.response(item.messages)

    return StreamingResponse(stream_generator(response), media_type="text/event-stream")
