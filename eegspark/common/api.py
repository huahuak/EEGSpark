from typing import Callable, List

from pyspark import RDD
from eegspark.data import fetcher, provider
from eegspark.algor import algor
from eegspark.function import func
import eegspark.common.eegspark as eegspark


def load(source: fetcher.Source):
    rdd = lambda: provider.Source2Rdd(source)
    return Pipeline(rdd)


class Pipeline:
    def __init__(self, input: Callable) -> None:
        self.inRDD = input
        self.algors: List[algor.Algor] = []

    def algor(self, algor: algor.Algor):
        self.algors.append(algor)
        return self

    def exec(self, func: func.Func):
        result: RDD = None
        result.map()
        for al in self.algors:
            result = al.execute(self.inRDD())
        result = func.execute(result)
        return result
