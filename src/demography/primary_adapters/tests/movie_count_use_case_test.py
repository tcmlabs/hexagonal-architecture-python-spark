from pyspark.sql import SparkSession
from demography.core.ports.primary.count_movie_command import CountMovieCommand

from demography.core.use_cases.count_movie_use_case import CountMovieUseCase
from demography.secondary_adapters.repositories.movie.in_memory_movie_repository import (
    InMemoryMovieRepository,
)


class TestMovieCountUseCase:
    def test_total_number_of_movies(self, spark_session: SparkSession):
        movie_repository = InMemoryMovieRepository(spark_session)
        count_movie_use_case = CountMovieUseCase(movie_repository)

        average_movie_budget_command = CountMovieCommand()

        total_number_of_movies = count_movie_use_case.run(average_movie_budget_command)

        assert total_number_of_movies == 3
