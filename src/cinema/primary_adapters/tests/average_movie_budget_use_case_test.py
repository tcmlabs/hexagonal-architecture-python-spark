from pyspark.sql import SparkSession
from cinema.core.ports.primary.average_movie_budget_command import (
    AverageMovieBudgetCommand,
)
from cinema.core.use_cases.average_budget_use_case import AverageMovieBudgetUseCase
from cinema.secondary_adapters.repositories.movie.in_memory_movie_repository import (
    InMemoryMovieRepository,
)


class TestAverageMovieBudgetUseCase:
    def test_average_movie_budget(self, spark_session: SparkSession):
        movie_repository = InMemoryMovieRepository(spark_session)
        average_movie_budget_use_case = AverageMovieBudgetUseCase(movie_repository)

        average_movie_budget_command = AverageMovieBudgetCommand()

        average_budget = average_movie_budget_use_case.run(average_movie_budget_command)

        assert average_budget == 135_000_000
