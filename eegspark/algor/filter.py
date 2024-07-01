from typing import Callable
from eegspark.algor.algor import Algor
from scipy.signal import butter, lfilter, freqz


class LowPassFilter(Algor):
    def __init__(self, lowpass, fs) -> None:
        super().__init__()
        self.lowpass_cutoff = lowpass  # 低通截止频率
        self.fs = fs

    @staticmethod
    def butter_lowpass(data, cutoff, fs, order=4):
        nyquist = 0.5 * fs
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype="low", analog=False)
        y = lfilter(b, a, data)
        return y

    @staticmethod
    def butter_lowpass_element(data, cutoff, fs, order=4):
        # 这个函数处理单个元素（数组）
        return LowPassFilter.butter_lowpass(data, cutoff, fs, order)

    def function(self) -> Callable:
        # x = ch
        # return lambda x: LowPassFilter.butter_lowpass_element(x, self.lowpass_cutoff, self.fs)
        return lambda x: LowPassFilter.butter_lowpass(x, self.lowpass_cutoff, self.fs)


class HighPassFilter(Algor):
    def __init__(self, highpass, fs) -> None:
        super().__init__()
        self.highpass_cutoff = highpass  # 高通截止频率
        self.fs = fs

    @staticmethod
    def butter_highpass(data, cutoff, fs, order=4):
        nyquist = 0.5 * fs
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype="high", analog=False)
        y = lfilter(b, a, data)
        return y

    @staticmethod
    def butter_highpass_element(data, cutoff, fs, order=4):
        # 这个函数处理单个元素（数组）
        return HighPassFilter.butter_highpass(data, cutoff, fs, order)

    def function(self) -> Callable:
        # x = ch
        # return lambda x: HighPassFilter.butter_highpass_element(x, self.highpass_cutoff, self.fs)
        return lambda x: HighPassFilter.butter_highpass(
            x, self.highpass_cutoff, self.fs
        )
