from cinema.core.domain.movie_type import Movie
from cinema.core.ports.primary.most_expensive_movie_command import (
    MostExpensiveMoviesCommand,
)
from cinema.core.use_cases.most_expensive_movies import MostExpensiveMoviesUseCase
from cinema.secondary_adapters.repositories.movie.kaggle_movie_repository import (
    KaggleFileSystemMovieRepository,
)
from cinema.secondary_adapters.repositories.movie.in_memory_movie_repository import (
    InMemoryMovieRepository,
)
from pyspark.sql import SparkSession


class TestMostExpensiveMoviesUseCase:
    def test_most_expensive_movies(self, spark_session: SparkSession):
        movie_repository = InMemoryMovieRepository(spark_session)
        most_expensive_movies_use_case = MostExpensiveMoviesUseCase(movie_repository)

        most_expensive_movie_ever_command = MostExpensiveMoviesCommand(count=1)

        movie = most_expensive_movies_use_case.run(most_expensive_movie_ever_command)

        assert movie == [
            Movie(
                name="Strange Universe",
                budget=205_000_000,
            )
        ]

    def test_most_expensive_movies_kaggle_dataset(self, spark_session: SparkSession):
        movie_repository = KaggleFileSystemMovieRepository(spark_session)
        most_expensive_movies_use_case = MostExpensiveMoviesUseCase(movie_repository)

        most_expensive_movie_ever_command = MostExpensiveMoviesCommand(count=1)

        [movie] = most_expensive_movies_use_case.run(most_expensive_movie_ever_command)

        assert movie.name == "Pirates of the Caribbean: On Stranger Tides"
        assert movie.budget == 380_000_000
