from .model import Model


class Qwen(Model):
    def __init__(self, api_key: str, model: str) -> None:
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"

        super().__init__(api_key, base_url, model)
