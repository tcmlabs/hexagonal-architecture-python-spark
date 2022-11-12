from cinema.core.ports.primary.use_cases import UseCase
from cinema.core.ports.primary.average_movie_budget_command import (
    AverageMovieBudgetCommand,
)
from cinema.core.ports.secondary.movie_repository import MovieRepository


class AverageMovieBudgetUseCase(UseCase[AverageMovieBudgetCommand, float]):
    # https://stackoverflow.com/questions/72141966/infer-type-from-subclass-method-return-type

    def __init__(self, movie_repository: MovieRepository) -> None:
        self._movie_repository = movie_repository

    def run(self, command: AverageMovieBudgetCommand):
        # TODO: find out why we need to type 'command' argument again
        # NOTE: this could also be implemented with a 'domain service' instead of a DSL
        average_movie_budget = self._movie_repository.find_all_movies().average_budget()

        return average_movie_budget
