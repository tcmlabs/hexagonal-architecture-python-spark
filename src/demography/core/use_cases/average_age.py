from demography.core.ports.secondary.person_repository import PersonRepository


class AverageAgeUseCase:
    def __init__(self, person_repository: PersonRepository) -> None:
        self._person_repository = person_repository

    def run(self):
        average_age = self._person_repository.find_all_persons().average_age()

        return average_age
