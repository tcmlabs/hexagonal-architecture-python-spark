from pyspark.sql import SparkSession
from pyspark.sql import Row

from demography.secondary_adapters.repositories.person.in_memory_person_repository import (
    InMemoryPersonRepository,
)


def test_count_female_persons(spark_session: SparkSession):
    repository = InMemoryPersonRepository(spark_session)

    total = repository.find_all_persons().females().count()

    assert total == 2


def test_find_first_people_named_alice(spark_session: SparkSession):
    repository = InMemoryPersonRepository(spark_session)

    alices = repository.find_all_persons().named("Alice").gender().df.collect()[0]

    assert alices == Row(gender="female")
