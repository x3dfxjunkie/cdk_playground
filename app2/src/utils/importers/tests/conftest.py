import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark_session(request):
    spark = (
        SparkSession.builder.master("local[*]")
        .appName("identity_dyanamodb-streams_s3_importer")
        .config("spark.jars.packages", "graphframes:graphframes:0.8.2-spark3.2-s_2.12")
        .getOrCreate()
    )

    request.addfinalizer(lambda: spark.sparkContext.stop())

    return spark
