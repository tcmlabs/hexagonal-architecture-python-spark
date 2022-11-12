from abc import abstractmethod
from typing import Protocol

from pyspark.sql.dataframe import DataFrame


class MovieRepository(Protocol):
    @abstractmethod
    def find_all_movies(self) -> DataFrame:
        raise NotImplementedError()
