from pyspark.sql import SparkSession
from demography.core.ports.primary.most_expensive_movie_command import (
    MostExpensiveMoviesCommand,
)


from demography.secondary_adapters.repositories.movie.in_memory_movie_repository import (
    InMemoryMovieRepository,
)

from demography.core.use_cases.most_expensive_movies import MostExpensiveMoviesUseCase


def run_movie_application():
    # Wire-up dependencies
    spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

    movie_repository = InMemoryMovieRepository(spark)
    use_case = MostExpensiveMoviesUseCase(movie_repository)

    # Run use case
    top_two_most_expensive_movies = use_case.run(MostExpensiveMoviesCommand(count=2))

    return top_two_most_expensive_movies
