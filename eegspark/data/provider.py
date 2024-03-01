from eegspark.data.fetcher import Source
import eegspark.data.converter as conv
import eegspark.common.eegspark as eegspark
from eegspark.common.config import config
from pyspark import RDD


def Source2Rdd(source: Source) -> RDD:
    # now only single file
    files = [source.target]

    sc = eegspark.spark_session().sparkContext

    if config().fake:
        rdd = sc.parallelize(conv.fake())
        return rdd

    # read from .mat file
    rdd = sc.parallelize(files)
    rdd = rdd.map(conv.load_mat_file)

    return rdd