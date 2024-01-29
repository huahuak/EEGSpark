from pyspark.sql import SparkSession

_spark: SparkSession = None


def spark_session() -> SparkSession:
    if _spark != None:
        return _spark
    _spark = SparkSession.builder.appName("EEGSpark").getOrCreate()
    return _spark
