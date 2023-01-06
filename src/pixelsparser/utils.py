import json
from .Pixel import Pixel


def load(path: str) -> list:
    with open(path, "r", encoding="utf8") as f:
        data = json.load(f)
        return [Pixel(**pixel) for pixel in data]
