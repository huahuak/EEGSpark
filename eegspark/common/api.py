from typing import Callable
from pyspark import RDD
from eegspark.data import fetcher, provider


class EEGRDD(RDD):
    def __init__(self, source: fetcher.Source):
        self.sourceRDD = provider.Source2Rdd(source)

    def map(self, f: Callable) -> RDD:
        return self.sourceRDD.map(f)