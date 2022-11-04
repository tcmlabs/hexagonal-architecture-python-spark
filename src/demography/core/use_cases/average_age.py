from typing import Union
from demography.core.ports.primary.use_cases import UseCase
from demography.core.ports.primary.average_age_command import AverageAgeCommand
from demography.core.ports.secondary.person_repository import PersonRepository


class AverageAgeUseCase(UseCase[AverageAgeCommand, Union[float, int]]):
    # https://stackoverflow.com/questions/72141966/infer-type-from-subclass-method-return-type

    def __init__(self, person_repository: PersonRepository) -> None:
        self._person_repository = person_repository

    def run(self, command: AverageAgeCommand):
        # TODO: find out why we need to type 'command' argument again
        # NOTE: this could also be implemented with a 'domain service' instead of a DSL
        average_age = self._person_repository.find_all_persons().average_age()

        if command.should_round:
            return round(average_age)

        return average_age
