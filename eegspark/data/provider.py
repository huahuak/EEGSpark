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
    rdd = sc.parallelize(files)
    rdd = rdd.map(conv.load_mat_file)

    eRDD = EEGRDD(rdd)

    return eRDD
