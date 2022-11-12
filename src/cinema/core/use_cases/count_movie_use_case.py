from cinema.core.domain.movie_type import Movie
from cinema.core.domain.services.movie_domain_service import MovieDomainService
from cinema.core.ports.primary.count_movie_command import CountMovieCommand
from cinema.core.ports.primary.use_cases import UseCase
from cinema.core.ports.secondary.movie_repository import MovieRepository


class CountMovieUseCase(UseCase[CountMovieCommand, int]):
    # https://stackoverflow.com/questions/72141966/infer-type-from-subclass-method-return-type

    def __init__(self, movie_repository: MovieRepository) -> None:
        self._movie_repository = movie_repository

    def run(self, command: CountMovieCommand):
        # TODO: find out why we need to type 'command' argument again
        movies = MovieDomainService[Movie](self._movie_repository.find_all_movies())

        average_movie_budget = movies.count()

        return average_movie_budget
