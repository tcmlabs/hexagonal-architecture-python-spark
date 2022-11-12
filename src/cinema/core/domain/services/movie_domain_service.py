from __future__ import annotations

from typing import Generic, List, TypeVar

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, avg

from cinema.core.domain.movie_type import Movie, WithBudget, WithName

T = TypeVar("T", covariant=True)


class MovieDomainService(Generic[T]):
    df: DataFrame

    def __init__(self, df: DataFrame):
        self.df = df

    # Where steps
    def most_expensive(
        self: MovieDomainService[WithBudget], count: int
    ) -> MovieDomainService[T]:
        return MovieDomainService(self.df.orderBy(col("budget").desc()).limit(count))

    # Select
    def names(self: MovieDomainService[WithName]) -> MovieDomainService[WithName]:
        return MovieDomainService(self.df.select("name"))

    def budgets(self: MovieDomainService[WithBudget]) -> MovieDomainService[WithBudget]:
        return MovieDomainService(self.df.select("budget"))

    # Aggregations
    def average_budget(self: MovieDomainService[WithBudget]) -> float:
        return self.df.agg(avg(col("budget"))).collect()[0]["avg(budget)"]

    def count(self: MovieDomainService[T]) -> int:
        return self.df.count()

    # Terminal steps
    def dangerously_convert_to_list(self: MovieDomainService[Movie]) -> List[Movie]:
        # Note: Spark being a big data tool, we're not supposed to convert
        # a DataFrame to a list.
        # Such conversion is most likely an anti-pattern unless you're
        # absolutely sure that the Spark queries return a very small number of
        # elements
        movies = [Movie(**row.asDict()) for row in self.df.collect()]

        return movies
