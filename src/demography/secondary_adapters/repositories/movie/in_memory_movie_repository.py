from pyspark.sql import Row
from pyspark.sql import SparkSession

from demography.core.ports.secondary.movie_repository import MovieRepository

from demography.core.domain.services.movie_service import MovieDSL
from demography.core.domain.movie_type import Movie


class InMemoryMovieRepository(MovieRepository):
    spark: SparkSession

    def __init__(self, spark: SparkSession) -> None:
        super().__init__()
        self._spark = spark

    def find_all_movies(self) -> MovieDSL[Movie]:
        movies = self._spark.createDataFrame(
            [
                Row(
                    name="Greatest Heroes I",
                    budget=120_000_000,
                ),
                Row(
                    name="From the future, to the past",
                    budget=80_000_000,
                ),
                Row(
                    name="Strange Universe",
                    budget=205_000_000,
                ),
            ]
        )

        return MovieDSL[Movie](movies)
