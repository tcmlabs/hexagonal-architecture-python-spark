from __future__ import annotations

from pyspark.sql.dataframe import DataFrame


def say_hello(content: str):
    return f"Hello World! {content}"


def count_lines(df: DataFrame):
    return df.count()
