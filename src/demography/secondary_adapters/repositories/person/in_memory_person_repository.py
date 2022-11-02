from pyspark.sql import Row
from pyspark.sql import SparkSession

from demography.core.ports.secondary.person_repository import PersonRepository

from demography.core.domain.services.person_service import PersonsDSL
from demography.core.domain.person_type import Person


class InMemoryPersonRepository(PersonRepository):
    spark: SparkSession

    def __init__(self, spark: SparkSession) -> None:
        super().__init__()
        self._spark = spark

    def find_all_persons(self) -> PersonsDSL[Person]:
        persons = self._spark.createDataFrame(
            [
                Row(
                    name="Alice",
                    gender="female",
                    age=22,
                ),
                Row(
                    name="Bob",
                    gender="male",
                    age=20,
                ),
                Row(
                    name="Carol",
                    gender="female",
                    age=23,
                ),
            ]
        )

        return PersonsDSL[Person](persons)
