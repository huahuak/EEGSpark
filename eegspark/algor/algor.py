from typing import Callable
from eegspark.common.eegspark import error


class Algor:
    def __init__(self) -> None:
        pass

    def function() -> Callable:
        # must be impl by sub-class
        error("the algorithm not found!")

    def __call__(self) -> Callable:
        return self.function()