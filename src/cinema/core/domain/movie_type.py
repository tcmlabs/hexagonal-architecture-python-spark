from dataclasses import dataclass
from typing import Protocol


class WithName(Protocol):
    name: str


class WithBudget(Protocol):
    budget: int


@dataclass
class Movie(WithName, WithBudget):
    name: str
    budget: int
