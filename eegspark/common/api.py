from eegspark.data import fetcher, provider
from eegspark.algor import algor
from eegspark.function import func

class Pipeline:
    @staticmethod
    def load(source: fetcher.Source):
        lambda: provider.Source2Rdd(source)
        return Pipeline()

    def algor(self, algor: algor.Algor):
        # algor.execute()
        return self

    def func(self, func: func.Func):
        return self

    def exec(self):
        pass
