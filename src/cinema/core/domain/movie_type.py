from typing import TypedDict


class WithName(TypedDict):
    name: str


class WithBudget(TypedDict):
    budget: int


class Movie(WithName, WithBudget):
    pass
