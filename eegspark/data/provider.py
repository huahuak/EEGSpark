from eegspark.data.fetcher import Source
import eegspark.data.converter as conv
import eegspark.common.eegspark as eegspark
from eegspark.common.eegrdd import EEGRDD
from eegspark.common.config import config


def Source2EEGRDD(source: Source) -> "EEGRDD":
    # now only single file
    files = [source.target]

    sc = eegspark.spark_session().sparkContext

    if config().fake:
        rdd = sc.parallelize(conv.fake())
        return rdd

    # read from .mat file
    rdd = sc.parallelize(files) # RDD: [file]
    rdd = rdd.flatMap(conv.load_mat_file) # [file] - map -> [[ch, ch]] - flat -> [ch, ch]

    # times [timeStamp] 

    eRDD = EEGRDD(rdd)

    return eRDD
