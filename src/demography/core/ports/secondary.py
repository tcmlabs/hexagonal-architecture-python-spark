from abc import abstractmethod
from typing import Protocol

from demography.core.domain.services.person_service import PersonsDSL
from demography.core.domain.person_type import Person


class PersonRepository(Protocol):
    @abstractmethod
    def find_all_persons(self) -> PersonsDSL[Person]:
        raise NotImplementedError()
