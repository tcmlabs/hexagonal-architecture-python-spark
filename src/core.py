from __future__ import annotations

from typing import Generic, Literal, TypeVar, TypedDict
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, avg


def say_hello(content: str):
    return f"Hello World! {content}"


def count_lines(df: DataFrame):
    return df.count()


class Named(TypedDict):
    name: str


class Gendered(TypedDict):
    gender: Literal["male", "female"]


class Aged(TypedDict):
    age: int


class Person(Named, Gendered, Aged):
    pass


T = TypeVar("T", covariant=True)


class PersonsDSL(Generic[T]):
    df: DataFrame

    def __init__(self, df: DataFrame):
        self.df = df

    # Where
    def females(self: PersonsDSL[Gendered]) -> PersonsDSL[T]:  # ok
        return PersonsDSL(self.df.filter(self.df.gender == "female"))

    def named(self: PersonsDSL[Named], named: str) -> PersonsDSL[T]:
        return PersonsDSL(self.df.filter(self.df.name == named))

    # Select
    def names(self: PersonsDSL[Named]) -> PersonsDSL[Named]:
        return PersonsDSL(self.df.select("name"))

    def gender(self: PersonsDSL[Gendered]) -> PersonsDSL[Gendered]:
        return PersonsDSL(self.df.select("gender"))

    # Aggregations
    def average_age(self: PersonsDSL[Aged]) -> float:
        return self.df.agg(avg(col("age"))).collect()[0]["avg(age)"]

    def count(self: PersonsDSL[T]) -> int:
        return self.df.count()
