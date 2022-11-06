from typing import final

from cinema.core.domain.movie_type import Movie
from cinema.core.domain.services.movie_service import MovieDSL
from cinema.core.ports.secondary.movie_repository import MovieRepository
from pyspark.sql import SparkSession
from pyspark.sql.types import DateType, FloatType, IntegerType, StringType, StructType

movies_metadata_raw_csv_schema = (
    StructType()
    .add("adult", StringType(), nullable=False)
    .add("belongs_to_collection", StringType(), nullable=False)
    .add("budget", IntegerType(), nullable=False)
    .add("genres", StringType(), nullable=False)
    .add("homepage", StringType(), nullable=False)
    .add("id", StringType(), nullable=False)
    .add("imdb_id", StringType(), nullable=False)
    .add("original_language", StringType(), nullable=False)
    .add("original_title", StringType(), nullable=False)
    .add("overview", StringType(), nullable=False)
    .add("popularity", FloatType(), nullable=False)
    .add("poster_path", StringType(), nullable=False)
    .add("production_companies", StringType(), nullable=False)
    .add("production_countries", StringType(), nullable=False)
    .add("release_date", DateType(), nullable=False)
    .add("revenue", IntegerType(), nullable=False)
    .add("runtime", FloatType(), nullable=False)
    .add("spoken_languages", StringType(), nullable=False)
    .add("status", StringType(), nullable=False)
    .add("tagline", StringType(), nullable=False)
    .add("title", StringType(), nullable=False)
    .add("video", StringType(), nullable=False)
    .add("vote_average", FloatType(), nullable=False)
    .add("vote_count", IntegerType(), nullable=False)
)


@final
class FileSystemMovieRepository(MovieRepository):
    spark: SparkSession

    def __init__(self, spark: SparkSession) -> None:
        self._spark = spark

    def find_all_movies(self) -> MovieDSL[Movie]:
        movies = self._spark.read.csv(
            "data/kaggle_movies_dataset/movies_metadata.csv",
            # See: https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option
            schema=movies_metadata_raw_csv_schema,
            header=True,
            inferSchema=False,
            mode="PERMISSIVE",  # stricter: FAILFAST
            sep=",",
        ).withColumnRenamed("original_title", "name")

        return MovieDSL[Movie](movies)
