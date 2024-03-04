from typing import Callable
from pyspark import RDD

class EEGRDD:
    def __init__(self, data: RDD):
        self.dataRDD = data

    def map(self, f: Callable) -> "EEGRDD":
        return EEGRDD(self.dataRDD.map(f))

    def foreach(self, f: Callable) -> None:
        self.dataRDD.foreach(f)
