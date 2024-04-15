from eegspark.data.fetcher import Source
import eegspark.data.converter as conv
import eegspark.common.eegspark as eegspark
from eegspark.common.eegrdd import EEGRDD
from eegspark.common.config import config
from pyspark import SparkContext


def process_file(file_path):
    # 移除对 SparkContext 参数的引用
    if config().fake:
        # Your logic for fake data goes here
        pass
    else:
        source = Source(file_path)  # 使用 file_path 创建 Source 实例
        raw_data = source.load_data()
        data = raw_data.get_data()
        times = raw_data.times
        # 调用convert_to_rdd函数，而不是传递sc参数
        rdd_channel_data, rdd_time_data = conv.convert_to_rdd(data, times)
        return rdd_channel_data, rdd_time_data


def Source2EEGRDD(file_paths: list) -> EEGRDD:
    sc = SparkContext.getOrCreate()  # 获取现有的 SparkContext 或创建新的

    # 创建文件路径与索引的配对，以便在后面能够区分数据来源于哪个文件
    indexed_file_paths = list(enumerate(file_paths))

    # 将路径列表并行化，包括它们的索引
    files_rdd = sc.parallelize(indexed_file_paths)

    # 使用flatMapValues对每个文件调用process_file，并且保留文件索引
    indexed_rdd_results = files_rdd.flatMapValues(lambda file_index_and_path: process_file(file_index_and_path[1]))

    # 将结果数据和文件索引分离
    rdd_channel_data = indexed_rdd_results.map(lambda indexed_data: (indexed_data[0], indexed_data[1][0]))
    rdd_time_data = indexed_rdd_results.map(lambda indexed_data: (indexed_data[0], indexed_data[1][1]))

    # 用文件索引标识的RDD数据被赋予EEGRDD，这样数据就会按文件区分
    eeg_rdd = EEGRDD(rdd_channel_data, rdd_time_data)
    return eeg_rdd

# 注意: 根据EEGRDD的定义，如果EEGRDD不能接受元组形式的RDD，需要对EEGRDD的结构进行相应的修改。