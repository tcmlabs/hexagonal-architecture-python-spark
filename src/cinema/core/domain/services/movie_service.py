from __future__ import annotations

from typing import Generic, List, TypeVar

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, avg

from cinema.core.domain.movie_type import Movie, WithBudget, WithName

T = TypeVar("T", covariant=True)


class MovieDSL(Generic[T]):
    df: DataFrame

    def __init__(self, df: DataFrame):
        self.df = df

    # Where steps
    def most_expensive(self: MovieDSL[WithBudget], count: int) -> MovieDSL[T]:
        return MovieDSL(self.df.orderBy(col("budget").desc()).limit(count))

    # Select
    def names(self: MovieDSL[WithName]) -> MovieDSL[WithName]:
        return MovieDSL(self.df.select("name"))

    def budgets(self: MovieDSL[WithBudget]) -> MovieDSL[WithBudget]:
        return MovieDSL(self.df.select("budget"))

    # Aggregations
    def average_budget(self: MovieDSL[WithBudget]) -> float:
        return self.df.agg(avg(col("budget"))).collect()[0]["avg(budget)"]

    def count(self: MovieDSL[T]) -> int:
        return self.df.count()

    # Terminal steps
    def dangerously_convert_to_list(self: MovieDSL[Movie]) -> List[Movie]:
        # Note: Spark being a big data tool, we're not supposed to convert
        # a DataFrame to a list.
        # Such conversion is most likely an anti-pattern unless you're
        # absolutely sure that the Spark queries return a very small number of
        # elements
        movies = [Movie(**row.asDict()) for row in self.df.collect()]

        return movies