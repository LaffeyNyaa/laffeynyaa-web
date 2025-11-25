from .qwen import Qwen


class QwenFlash(Qwen):
    def __init__(self, api_key: str) -> None:
        super().__init__(api_key, "qwen-flash")
