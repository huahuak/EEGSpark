import scipy.io as sio
from eegspark.common.eegspark import error
from pyspark import SparkContext
import numpy as np


def load_mat_file(file_path: str):
    try:
        mat_contents = sio.loadmat(file_path)
        # 返回包含数据和时间向量的字典
        return {
            "data": mat_contents["data"] if "data" in mat_contents else None,
            "times": mat_contents["times"] if "times" in mat_contents else None,
        }
    except FileNotFoundError:
        error(f"File not found: {file_path}")
        return None
    except sio.matlab.miobase.MatReadError as e:
        error(f"MAT file read error: {e}")
        return None
    except Exception as e:
        error(f"Error occurred while loading EEG data: {e}")
        return None


def convert_to_rdd(data, times, sc: SparkContext):
    if not sc or not isinstance(data, np.ndarray) or not isinstance(times, np.ndarray):
        raise ValueError(
            "A valid SparkContext, numpy.ndarray for data, \
                         and numpy.ndarray for times are required."
        )
    # Data（一个2D numpy array，每行代表一个通道的数据）
    rdd_channel_data = sc.parallelize(data.tolist())  # 将每个通道的数据转换成RDD

    # 转换时间数据为列表
    time_data = times.tolist()

    # 使用SparkContext创建包含时间数据的RDD
    rdd_time_data = sc.parallelize(
        time_data
    )  # Not wrapping in a list as it's already a list of time points

    return rdd_channel_data, rdd_time_data


def fake():
    fs = 1000  # 采样频率
    t = np.arange(0, 1, 1 / fs)  # 时间向量
    signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)
    return [signal]  # [ch] [[1, 2, 4, 5]]
