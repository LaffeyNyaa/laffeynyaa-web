from typing import Iterable
from openai import OpenAI, Stream
from openai.types.chat import ChatCompletionChunk, ChatCompletionMessageParam


class Model:
    def __init__(self, api_key: str, base_url: str, model: str) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def response(
        self, messages: Iterable[ChatCompletionMessageParam]
    ) -> Stream[ChatCompletionChunk]:
        return self.client.chat.completions.create(
            model=self.model, messages=messages, stream=True
        )

    @staticmethod
    def print_stream_response(response: Stream[ChatCompletionChunk]) -> None:
        for chunk in response:
            if chunk.choices:
                print(chunk.choices[0].delta.content, end="", flush=True)
