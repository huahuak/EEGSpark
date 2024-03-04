import eegspark.data.fetcher as fetcher
from eegspark.algor.filter import LowPassFilter
from eegspark.data.provider import Source2EEGRDD


source = fetcher.Source("data/subject_01_PC.mat")
lowpass = LowPassFilter(lowpass=30, fs=1000)

rdd = Source2EEGRDD(source)  # [ch]
rdd.foreach(lambda x: print(x[0:5]))
rdd.map(lowpass()).foreach(lambda x: print(x[0:5]))
