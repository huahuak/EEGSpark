from pyspark.rdd import RDD


class Algor:
    def __init__(self) -> None:
        pass
    
    def execute(input: RDD) -> RDD:
        # must be impl by sub-class
        raise Exception("the algorithm not found!")
