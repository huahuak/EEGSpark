import sys
import traceback

sys.path.append("/home/team4spark/EEGSpark")
from fetcher import Source
import converter as conv
from pyspark import SparkContext, SparkConf

# 基于你的配置初始化SparkContext
conf = SparkConf().setAppName("EEGRDDTest").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)


# 测试函数
def test_source2eegrdd():
    try:
        # 测试的文件路径列表
        file_paths = [
            '/home/team4spark/EEGSpark/data/S001R01.edf',
            '/home/team4spark/EEGSpark/data/subject_02_PC.mat'
        ]
        # 初始化一个空的RDD来存储最终的结果
        final_rdd = sc.emptyRDD()
        print("开始并行处理文件...")
        for file_path in file_paths:
            source = Source(file_path)
            raw_data = source.load_data()
            # 获取 MNE 对象的数据和时间
            channel_data = raw_data.get_data()
            times = raw_data.times
            # 调用convert_to_rdd函数，将EEG数据和时间转换成RDD
            rdd_channel_data, rdd_time_data = conv.convert_to_rdd(channel_data, times, sc)
            # 组合每个文件的RDD到最终的RDD中
            final_rdd = final_rdd.union(rdd_channel_data).union(rdd_time_data)

        print("并行处理文件成功。")
        # 通过action操作，例如count，来触发实际的计算
        print("开始对结果RDD进行计算...")
        count = final_rdd.count()
        print(f"结果RDD中的元素数量: {count}")
    except Exception as e:
        # 如果出现异常，打印异常信息
        print("出现了一个错误：", e)
        traceback.print_exc()
    finally:
        # 停止SparkContext
        sc.stop()


if __name__ == "__main__":
    test_source2eegrdd()