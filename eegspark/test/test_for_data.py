import sys
import traceback
from pyspark import SparkContext

sys.path.append("/home/team4spark/EEGSpark")
from eegspark.data.fetcher import Source
from eegspark.data.converter import converter as conv

# 请确保EEGRDD类被正确定义，可以处理两个RDD参数
from eegspark.common.eegrdd import EEGRDD
from eegspark.common.config import config
from pyspark.rdd import RDD

# 设置测试文件路径
test_file_path = "/home/team4spark/EEGSpark/data/subject_02_PC.mat"

# 初始化SparkContext
sc = SparkContext(appName="EEGRDDTest")


def test_fetcher():
    print("Testing fetcher...")
    try:
        source = Source(test_file_path)
        raw_data = source.load_data()
        print("Fetcher output (example channel data):")
        print(raw_data.get_data(picks=0)[:5])
        print("Fetcher passed!")
        return raw_data
    except Exception as e:
        print("Fetcher failed!")
        print(traceback.format_exc())


def test_converter(raw_data):
    print("Testing converter...")
    try:
        data = raw_data.get_data()
        times = raw_data.times
        # Assumes convert_to_rdd function is defined correctly in converter module
        rdd_channel_data, rdd_time_data = conv.convert_to_rdd(data, times, sc)

        print("Converter output (first 5 channel data elements):")
        print(rdd_channel_data.take(1))
        print("Converter output (first 5 time data elements):")
        print(rdd_time_data.take(1))
        print("Converter passed!")
        return rdd_channel_data, rdd_time_data
    except Exception as e:
        print("Converter failed!")
        print(traceback.format_exc())


def test_provider(rdd_channel_data, rdd_time_data):
    print("Testing provider...")
    try:
        # Assumes EEGRDD class is correctly modified to accept two RDDs
        eeg_rdd = EEGRDD(rdd_channel_data, rdd_time_data)

        # Test the EEGRDD object by taking an RDD sample
        print("Provider output (EEGRDD channel data sample):")
        print(eeg_rdd.channelDataRDD.take(1))
        print("Provider output (EEGRDD time data sample):")
        print(eeg_rdd.timeDataRDD.take(5))
        print("Provider passed!")
    except Exception as e:
        print("Provider failed!")
        print(traceback.format_exc())


# Run the test functions
raw_data = test_fetcher()
if raw_data:
    rdd_channel_data, rdd_time_data = test_converter(raw_data)
    if rdd_channel_data and rdd_time_data:
        test_provider(rdd_channel_data, rdd_time_data)

# Stop the SparkContext
sc.stop()
