import eegspark.common.api as api
import eegspark.data.fetcher as fetcher
from eegspark.algor.algor import LowPassFilter


source = fetcher.Source("data/subject_01_PC.mat")
lowpass = LowPassFilter(lowpass=30, fs=1000)

rdd = api.EEGRDD(source)
rdd.sourceRDD.foreach(lambda x: print(x[0:5]))
rdd.map(lowpass()).foreach(lambda x: print(x[0:5]))
