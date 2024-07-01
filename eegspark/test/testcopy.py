import eegspark.data.fetcher as fetcher
from eegspark.algor.filter import LowPassFilter
from eegspark.data.provider import Source2EEGRDD
from scipy.signal import butter, lfilter
from eegspark.common import eegrdd
from eegspark.algor.plot import Plot
from eegspark.algor.filter import HighPassFilter


# 初始化数据源和低通滤波器
source = fetcher.Source("/home/team4spark/EEGSpark/data/subject_02_PC.mat")
# lowpass_filter = LowPassFilter(lowpass=30, fs=500)

# # 使用Source2EEGRDD将数据源转化为EEGRDD对象
eegrdd = Source2EEGRDD(source)
# # 将低通滤波器应用于EEGRDD数据
lowpass_filter = LowPassFilter(lowpass=30, fs=500)
filtered_eegrdd = eegrdd.map_channel(lowpass_filter())
# # 将高通滤波器应用于RDD数据
highpass_filter = HighPassFilter(highpass=0.5, fs=500)
filtered_eegrdd = filtered_eegrdd.map_channels_with_filter(highpass_filter.
    highpass_cutoff, fs=500)
# # 遍历EEGRDD的channelDataRDD并打印每个通道的前5个数据点
# # eegrdd.foreach_channel(lambda x: print(x[0:5]))

# 将低通滤波器应用到EEGRDD的channelDataRDD上，然后遍历并打印每个滤波后的通道的前5个数据点
# LowPassFilter类内有一个方法可以返回适合用于RDD.map的函数
# filtered_eegrdd = eegrdd.map_channels(lowpass_filter.function)
# filtered_eegrdd.foreach_channel(lambda x: print(x[0:5]))
eegrdd.foreach_channel(lambda x: print(x[0:5]))

filtered_eegrdd.foreach_channel(lambda x: print(x[0:5]))
filtered_eegrdd.foreach_channel(lambda x: print(x[0:5]))

plt = Plot(t = eegrdd.timeDataRDD.collect())
filtered_eegrdd.foreach_channel(plt())
