from typing import List

from cinema.core.domain.movie_type import Movie
from cinema.core.domain.services.movie_domain_service import MovieDomainService
from cinema.core.ports.primary.most_expensive_movie_command import (
    MostExpensiveMoviesCommand,
)
from cinema.core.ports.primary.use_cases import UseCase
from cinema.core.ports.secondary.movie_repository import MovieRepository


class MostExpensiveMoviesUseCase(UseCase[MostExpensiveMoviesCommand, List[Movie]]):
    # https://stackoverflow.com/questions/72141966/infer-type-from-subclass-method-return-type

    def __init__(self, movie_repository: MovieRepository) -> None:
        self._movie_repository = movie_repository

    def run(self, command: MostExpensiveMoviesCommand):
        # TODO: find out why we need to type 'command' argument again
        movies = MovieDomainService[Movie](self._movie_repository.find_all_movies())

        most_expensive_movies = movies.most_expensive(
            count=command.count
        ).dangerously_convert_to_list()

        return most_expensive_movies
