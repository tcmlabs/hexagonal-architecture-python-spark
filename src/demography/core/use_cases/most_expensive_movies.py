from typing import List
from demography.core.ports.primary.use_cases import UseCase
from demography.core.ports.primary.most_expensive_movie_command import (
    MostExpensiveMoviesCommand,
)
from demography.core.ports.secondary.movie_repository import MovieRepository
from demography.core.domain.movie_type import Movie


class MostExpensiveMoviesUseCase(UseCase[MostExpensiveMoviesCommand, List[Movie]]):
    # https://stackoverflow.com/questions/72141966/infer-type-from-subclass-method-return-type

    def __init__(self, movie_repository: MovieRepository) -> None:
        self._movie_repository = movie_repository

    def run(self, command: MostExpensiveMoviesCommand):
        # TODO: find out why we need to type 'command' argument again
        # NOTE: this could also be implemented with a 'domain service' instead of a DSL
        most_expensive_movies = (
            self._movie_repository.find_all_movies()
            .most_expensive(count=command.count)
            .dangerously_convert_to_list()
        )

        return most_expensive_movies
