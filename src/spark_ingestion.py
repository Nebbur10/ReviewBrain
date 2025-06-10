from pyspark.sql import SparkSession
import pandas as pd

def load_spark_data(file_path: str = "data/reviews.csv", sample_size: int = 10000) -> pd.DataFrame:
    spark = SparkSession.builder \
        .appName("ReviewBrain") \
        .master("local[*]") \
        .getOrCreate()

    df_spark = spark.read.option("header", "true").csv(file_path)

    df_spark = df_spark \
        .withColumnRenamed("reviews.rating", "reviews_rating") \
        .withColumnRenamed("reviews.text", "reviews_text")

    print("Columnas tras renombrar:")
    df_spark.printSchema()

    df_spark = df_spark.select("reviews_rating", "reviews_text", "name")

    df_spark = df_spark.na.drop(subset=["reviews_rating", "reviews_text", "name"])

    if df_spark.count() > sample_size:
        df_spark = df_spark.sample(fraction=sample_size / df_spark.count(), seed=42)

    df_pandas = df_spark.toPandas()

    df_pandas["reviews_rating"] = pd.to_numeric(df_pandas["reviews_rating"], errors="coerce")
    df_pandas = df_pandas.dropna(subset=["reviews_rating"])
    df_pandas["reviews_rating"] = df_pandas["reviews_rating"].astype(int)

    df_pandas = df_pandas.rename(columns={
        "reviews_rating": "rating",
        "reviews_text": "text"
    })

    return df_pandas
