from __future__ import annotations

from typing import Generic, TypeVar

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, avg

from demography.core.domain.person_type import Gendered, Named, Aged

T = TypeVar("T", covariant=True)


class PersonsDSL(Generic[T]):
    # A final encoding domain-specific language
    # Such DSL is expressed in terms of its concrete implementation.
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
