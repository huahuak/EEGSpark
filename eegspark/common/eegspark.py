from pyspark.sql import SparkSession

_spark: SparkSession = None


def spark_session() -> SparkSession:
    global _spark
    if _spark != None:
        return _spark
    _spark = SparkSession.builder.appName("EEGSpark").getOrCreate()
    return _spark


def error(str):
    print(str)

def info(str):
    print(str)