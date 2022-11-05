from pyspark.sql import SparkSession
from demography.core.domain.movie_type import Movie
from demography.core.ports.primary.most_expensive_movie_command import (
    MostExpensiveMoviesCommand,
)

from demography.core.use_cases.most_expensive_movies import MostExpensiveMoviesUseCase
from demography.secondary_adapters.repositories.movie.in_memory_movie_repository import (
    InMemoryMovieRepository,
)


def test_most_expensive_movies(spark_session: SparkSession):
    movie_repository = InMemoryMovieRepository(spark_session)
    most_expensive_movies_use_case = MostExpensiveMoviesUseCase(movie_repository)

    most_expensive_movie_ever_command = MostExpensiveMoviesCommand(count=1)

    movie = most_expensive_movies_use_case.run(most_expensive_movie_ever_command)

    assert movie == [
        Movie(
            name="Strange Universe",
            budget=200_000_000,
        )
    ]
