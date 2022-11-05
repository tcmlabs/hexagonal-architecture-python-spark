from abc import abstractmethod
from typing import Protocol

from demography.core.domain.services.movie_service import MovieDSL
from demography.core.domain.movie_type import Movie


class MovieRepository(Protocol):
    @abstractmethod
    def find_all_movies(self) -> MovieDSL[Movie]:
        raise NotImplementedError()
