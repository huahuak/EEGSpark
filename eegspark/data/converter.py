import scipy.io as sio
from eegspark.common.eegspark import error


def load_mat_file(file_path: str):
    """
    Load EEG data from a .mat file.

    Returns:
    - dict: A dictionary containing the 'data' array loaded from the .mat file.
    """
    try:
        data = sio.loadmat(file_path)
        return {"data": data["data"]} if "data" in data else {}
    except FileNotFoundError:
        error(f"File not found: {file_path}")
    except sio.matlab.miobase.MatReadError as e:
        error(f"MAT file read error: {e}")
    except Exception as e:
        error(f"Error occurred while loading EEG data: {e}")


import numpy as np


def fake():
    fs = 1000  # 采样频率
    t = np.arange(0, 1, 1 / fs)  # 时间向量
    signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 50 * t)
    return [signal]
