from pyspark import Row
from main import count_lines, say_hello

from datetime import datetime, date
from pyspark.sql import SparkSession
from pyspark.sql import Row


def test_hello_world():
    assert say_hello("Bob") == "Hello World! Bob"


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
