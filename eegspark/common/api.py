from typing import Callable
from pyspark import RDD
from eegspark.data import fetcher, provider


class EEGRDD:
    def __init__(self, rdd: RDD):
        self.rdd = rdd

    @classmethod
    def fromSource(cls, source: fetcher.Source) -> "EEGRDD":
        rdd = provider.Source2Rdd(source)
        return EEGRDD(rdd)

    def map(self, f: Callable) -> "EEGRDD":
        return EEGRDD(self.rdd.map(f))

    def foreach(self, f: Callable) -> None:
        self.rdd.foreach(f)
