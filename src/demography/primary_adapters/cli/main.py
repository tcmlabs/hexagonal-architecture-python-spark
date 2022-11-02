from pyspark.sql import SparkSession

from demography.secondary_adapters.repositories.person.file_system_person_repository import (
    FileSystemPersonRepository,
)

from demography.core.use_cases.average_age import AverageAgeUseCase


def run_person_application():
    # Wire-up dependencies
    spark = SparkSession.builder.appName("Python Spark SQL basic example").getOrCreate()

    person_repository = FileSystemPersonRepository(spark)
    use_case = AverageAgeUseCase(person_repository)

    # Run use case
    average_age = use_case.run()

    return average_age
