from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, ShortType, StringType

from demography.core.ports.secondary.person_repository import PersonRepository

from demography.core.domain.services.person_service import PersonsDSL
from demography.core.domain.person_type import Person


class FileSystemPersonRepository(PersonRepository):
    spark: SparkSession

    def __init__(self, spark: SparkSession) -> None:
        self._spark = spark

    def find_all_persons(self) -> PersonsDSL[Person]:
        schema = (
            StructType()
            .add("name", StringType(), nullable=False)
            .add("gender", StringType(), nullable=False)
            .add("age", ShortType(), nullable=False)
        )

        persons = self._spark.read.csv(
            "data/persons.csv",
            # See: https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option
            schema,
            header=True,
            inferSchema=False,
            mode="FAILFAST",
            sep=",",
        )

        return PersonsDSL[Person](persons)
