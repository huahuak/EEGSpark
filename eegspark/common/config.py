class Config:
    def __init__(self) -> None:
        self.fake = False
        pass

    def load_config_from_map(self, cfg):
        # load config from map
        pass

    def load_config_from_json(self, str):
        # load config from json str
        pass


_config = None


def config() -> Config:
    global _config
    if _config != None:
        return _config
    _config = Config()
    return _config
