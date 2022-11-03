from pyspark.sql import SparkSession
from demography.core.ports.primary.average_age_command import AverageAgeCommand

from demography.core.use_cases.average_age import AverageAgeUseCase
from demography.secondary_adapters.repositories.person.in_memory_person_repository import (
    InMemoryPersonRepository,
)


def test_calculate_average_age(spark_session: SparkSession):
    person_repository = InMemoryPersonRepository(spark_session)
    average_age_use_case = AverageAgeUseCase(person_repository)

    result = average_age_use_case.run(AverageAgeCommand(should_round=False))

    assert result == 21.666666666666668
