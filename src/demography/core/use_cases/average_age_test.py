from pyspark.sql import SparkSession

from demography.core.use_cases.average_age import AverageAgeUseCase
from demography.secondary_adapters.repositories.person.in_memory_person_repository import (
    InMemoryPersonRepository,
)


def test_calculate_average_age(spark_session: SparkSession):
    person_repository = InMemoryPersonRepository(spark_session)
    use_case = AverageAgeUseCase(person_repository)

    result = use_case.run()

    assert result == 21.666666666666668
