from __future__ import annotations

from typing import Generic, List, TypeVar

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col

from demography.core.domain.movie_type import Movie, WithBudget

T = TypeVar("T", covariant=True)


class MovieDSL(Generic[T]):
    df: DataFrame

    def __init__(self, df: DataFrame):
        self.df = df

    # Where steps
    def most_expensive(self: MovieDSL[WithBudget], count: int) -> MovieDSL[T]:
        return MovieDSL(self.df.orderBy(col("budget").desc()).limit(count))

    # Terminal steps
    def dangerously_convert_to_list(self: MovieDSL[Movie]) -> List[Movie]:
        # Note: Spark being a big data tool, we're not supposed to convert
        # a DataFrame to a list.
        # Such conversion is most likely an anti-pattern unless you're
        # absolutely sure that the Spark queries return a very small number of
        # elements
        movies = [Movie(**row.asDict()) for row in self.df.collect()]

        return movies
