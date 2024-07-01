from pyspark import RDD
from typing import Callable
from scipy.signal import butter, lfilter
import mne
import numpy as np
from mne.time_frequency import tfr_morlet

# 在 EEGRDD 类中，我们改造通道数据和时间数据以包括它们的文件索引。
# 每个元素现在是一个元组 (文件索引, 数据)
class EEGRDD:
    def __init__(self, channel_data: RDD, time_data: RDD):
        # 数据保存格式为 (文件索引, 通道数据)
        self.channelDataRDD = channel_data
        # 数据保存格式为 (文件索引, 时间数据)
        self.timeDataRDD = time_data

    def map_channel(self, f: Callable) -> "EEGRDD":
        # 应用函数 f 到每个通道数据上，同时保留索引
        mapped_channel_data = self.channelDataRDD.map(lambda indexed_data: (indexed_data[0], f(indexed_data[1])))
        return EEGRDD(mapped_channel_data, self.timeDataRDD)

    def foreach_channel(self, f: Callable) -> None:
        # 对每个通道数据执行函数 f，但没有返回值
        self.channelDataRDD.foreach(lambda indexed_data: f(indexed_data[1]))

    def map_channels_with_filter(self, cutoff, fs, order=4) -> "EEGRDD":
        # 初始化滤波器系数
        b, a = butter_lowpass_init(cutoff, fs, order)
        # 应用滤波器到每个通道，保持索引不变
        filtered_rdd = self.channelDataRDD.map(lambda indexed_data: (indexed_data[0], apply_butter_lowpass(indexed_data[1], b, a)))
        return EEGRDD(filtered_rdd, self.timeDataRDD)

def butter_lowpass_init(cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype="low", analog=False)
    return b, a


def apply_butter_lowpass(data, b, a):
    y = lfilter(b, a, data)
    return y
# 2024.04.12

def to_raw(self, ch_names, sfreq):
    raw_array = self.channelDataRDD.values().collect()
    raw_array = np.array(raw_array)
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=['eeg']*len(ch_names))
    raw = mne.io.RawArray(raw_array.T, info)
    return raw

def compute_time_frequency(self, ch_names, sfreq):
    raw = self.to_raw(ch_names, sfreq)
    freqs = np.arange(5, 70, 1)
    n_cycles = freqs / 2.
    power, times = mne.time_frequency.tfr_multitaper(raw, freqs=freqs, n_cycles=n_cycles, time_bandwidth=2, return_itc=False)
    return times, freqs, power