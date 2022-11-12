from cinema.core.ports.secondary.movie_repository import MovieRepository
from pyspark.sql import Row, SparkSession


class InMemoryMovieRepository(MovieRepository):
    spark: SparkSession

    def __init__(self, spark: SparkSession) -> None:
        super().__init__()
        self._spark = spark

    def find_all_movies(self):
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

        return movies
