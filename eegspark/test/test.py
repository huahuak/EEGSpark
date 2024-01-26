from eegspark.function.func import Func
from eegspark.algor.algor import Algor
from eegspark.common.api import Pipeline

Pipeline.load("file").algor(Algor()).func(Func()).exec()
