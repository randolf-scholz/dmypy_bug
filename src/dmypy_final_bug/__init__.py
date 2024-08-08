__all__ = ["ImmutablePoint", "MyDataClass"]

from typing import Final
from dataclasses import dataclass

import torch

@dataclass
class MyDataClass:
    foo: Final[int]
    bar: Final[int]


class ImmutablePoint:
    x: Final[int]
    y: Final[int]

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y
