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

    def function(self) -> Callable:
        # x = ch
        return lambda x: LowPassFilter.butter_lowpass(x, self.lowpass_cutoff, self.fs)


# class HighPassFilter