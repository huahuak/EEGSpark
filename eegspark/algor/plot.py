import matplotlib.pyplot as plt
import io
import base64
from typing import Callable
from eegspark.algor.algor import Algor


class Plot(Algor):
    def __init__(self, t) -> None:
        super().__init__()
        self.t = t

    @staticmethod
    def func_plt(data, t):
        # plt.figure(figsize=(a,b))
        # plt.plot(data, t, label='Filtered Signal', color='red')
        # plt.xlabel('Time')
        # plt.ylabel('Amplitude')
        fig, ax = plt.subplots()
        ax.plot(data, t)

        # 将图形对象转换为字节流
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        # 将字节流转换为base64编码的字符串
        encoded_image = base64.b64encode(buf.read()).decode("utf-8")

        plt.close()
        return encoded_image

    def function(self) -> Callable:
        # x = channel
        return lambda x: Plot.func_plt(x, self.t)
