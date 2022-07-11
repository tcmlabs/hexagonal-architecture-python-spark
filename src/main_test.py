from core import Person, PersonsDSL, count_lines, say_hello

from datetime import datetime, date
from pyspark.sql import SparkSession
from pyspark.sql import Row


def test_hello_world():
    assert say_hello("Bob") == "Hello World! Bob"


def test_count_female_persons():
    spark = SparkSession.builder.getOrCreate()

    persons = spark.createDataFrame(
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

    total = PersonsDSL[Person](persons).females().count()

    assert total == 2


def test_find_first_people_named_alice():
    spark = SparkSession.builder.getOrCreate()

    persons = spark.createDataFrame(
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

    alices = PersonsDSL[Person](persons).named("Alice").gender().df.collect()[0]

    assert alices == Row(gender="female")


def test_calculate_average_age():
    spark = SparkSession.builder.getOrCreate()

    persons = spark.createDataFrame(
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

    average_age = PersonsDSL[Person](persons).average_age()

    assert average_age == 21.666666666666668


def test_count_lines():
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame(
        [
            Row(
                a=1,
                b=2.0,
                c="string1",
                d=date(2000, 1, 1),
                e=datetime(2000, 1, 1, 12, 0),
            ),
            Row(
                a=2,
                b=3.0,
                c="string2",
                d=date(2000, 2, 1),
                e=datetime(2000, 1, 2, 12, 0),
            ),
            Row(
                a=4,
                b=5.0,
                c="string3",
                d=date(2000, 3, 1),
                e=datetime(2000, 1, 3, 12, 0),
            ),
        ]
    )

    assert count_lines(df) == 3
