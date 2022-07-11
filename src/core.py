from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Type, TypeVar
from pyspark.sql.dataframe import DataFrame


def say_hello(content):
    return f"Hello World! {content}"


def count_lines(df):
    return df.count()


@dataclass
class Person:
    name: str
    gender: str


TPersonsDSL = TypeVar("TPersonsDSL", bound="PersonsDSL")


class PersonsDSL:
    def __init__(self, df: DataFrame[Person]):
        self.df = df

    def females(self: TPersonsDSL) -> TPersonsDSL:
        return PersonsDSL(self.df.filter(self.df.gender == "female"))

    def names(self: TPersonsDSL) -> TPersonsDSL:
        return PersonsDSL(self.df.select("name"))

    def gender(self: TPersonsDSL) -> TPersonsDSL:
        return PersonsDSL(self.df.select("gender"))

    def count(self: TPersonsDSL) -> int:
        return self.df.count()
