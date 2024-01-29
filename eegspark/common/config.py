
class Config:
    def __init__(self) -> None:
        self.eeg_file_path = None
        pass

    def load_config_from_map(self, cfg):
        # load config from map
        pass
    
    def load_config_from_json(self, str):
        # load config from json str
        pass

    def eeg_file_path(self):
        return self.eeg_file_path