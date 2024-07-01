class Source:
    """
    Source describe how to fetch source file.
    """

    def __init__(self, target: str) -> None:
        """
        Initialize the Source object with the target path.
        """
        self.target = target