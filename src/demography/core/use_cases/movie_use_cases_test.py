from pyspark.sql import SparkSession
from demography.core.domain.movie_type import Movie
from demography.core.ports.primary.most_expensive_movie_command import (
    MostExpensiveMoviesCommand,
)
from demography.core.ports.primary.average_movie_budget_command import (
    AverageMovieBudgetCommand,
)
from demography.core.ports.primary.count_movie_command import CountMovieCommand

from demography.core.use_cases.most_expensive_movies import MostExpensiveMoviesUseCase
from demography.core.use_cases.average_budget_use_case import AverageMovieBudgetUseCase
from demography.core.use_cases.count_movie_use_case import CountMovieUseCase
from demography.secondary_adapters.repositories.movie.in_memory_movie_repository import (
    InMemoryMovieRepository,
)


class TestMovieUseCases:
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

    def test_average_budget(self, spark_session: SparkSession):
        movie_repository = InMemoryMovieRepository(spark_session)
        average_movie_budget_use_case = AverageMovieBudgetUseCase(movie_repository)

        average_movie_budget_command = AverageMovieBudgetCommand()

        average_budget = average_movie_budget_use_case.run(average_movie_budget_command)

        assert average_budget == 135_000_000

    def test_total_number_of_movies(self, spark_session: SparkSession):
        movie_repository = InMemoryMovieRepository(spark_session)
        count_movie_use_case = CountMovieUseCase(movie_repository)

        average_movie_budget_command = CountMovieCommand()

        total_number_of_movies = count_movie_use_case.run(average_movie_budget_command)

        assert total_number_of_movies == 3
