__all__ = ["ImmutablePoint", "MyDataClass", "MyModule"]

from typing import Final
from dataclasses import dataclass
import torch


@dataclass
class MyDataClass:
    x: Final[int]
    y: Final[int]


class ImmutablePoint:
    x: Final[int]
    y: Final[int]

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y


class MyModule(torch.nn.Module):
    x: Final[int]
    y: Final[int]

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self.x = x
        self.y = y
