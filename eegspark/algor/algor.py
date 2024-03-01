from typing import Callable
from scipy.signal import butter, lfilter, freqz


class Algor:
    def __init__(self) -> None:
        pass

    def function() -> Callable:
        # must be impl by sub-class
        raise Exception("the algorithm not found!")

    def __call__(self) -> Callable:
        return self.function()


class LowPassFilter(Algor):
    def __init__(self, lowpass, fs) -> None:
        super().__init__()
        self.lowpass_cutoff = lowpass  # 低通截止频率
        self.fs = fs

    @staticmethod
    def butter_lowpass(data, cutoff, fs, order=4):
        print(f"fs is {fs}")
        nyquist = 0.5 * fs
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype="low", analog=False)
        y = lfilter(b, a, data)
        return y

    def function(self) -> Callable:
        return lambda x: LowPassFilter.butter_lowpass(x, self.lowpass_cutoff, self.fs)
