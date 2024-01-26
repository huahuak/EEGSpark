from pyspark.rdd import RDD


class Func:
    def execute(input: RDD):
        # must be impl by sub-class
        raise Exception("the function not found!")
