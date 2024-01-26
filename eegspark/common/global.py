from pyspark.sql import SparkSession

_spark = None

def Spark():
    if _spark != None:
        return _spark
    _spark = SparkSession.builder.getOrCreate()
    