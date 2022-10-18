from typing import Literal, TypedDict


class Named(TypedDict):
    name: str


class Gendered(TypedDict):
    gender: Literal["male", "female"]


class Aged(TypedDict):
    age: int


class Person(Named, Gendered, Aged):
    pass
