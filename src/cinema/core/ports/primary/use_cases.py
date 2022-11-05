from abc import abstractmethod
from typing import Generic, Protocol, TypeVar


C = TypeVar("C", contravariant=True)  # Command
R = TypeVar("R", covariant=True)  # Response


class UseCase(Generic[C, R], Protocol):
    @abstractmethod
    def run(self, command: C) -> R:
        pass
