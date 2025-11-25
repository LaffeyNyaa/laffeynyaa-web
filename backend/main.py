import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Iterable
from openai.types.chat import ChatCompletionMessageParam
from .models.qwen_flash import QwenFlash


class Item(BaseModel):
    messages: Iterable[ChatCompletionMessageParam]


qwen_flash = QwenFlash(os.environ["DASHSCOPE_API_KEY"])


app = FastAPI()


@app.post("/")
async def root(item: Item):
    return qwen_flash.response(item.messages)
