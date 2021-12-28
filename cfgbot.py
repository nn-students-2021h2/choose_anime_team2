import json
import Path
class Configuration:
    _instance = None
    _properties = None
    def __new__(cls, *args, **kwargs):
        if not Configuration._instance:
            Configuration._instance = super(Configuration, cls).__new__(cls, *args, **kwargs)
        return Configuration._instance

    def __init__(self, fpath=None):
        self._file_path = fpath
        self._load_cfg()
        Configuration._properties = {}
        for name, i in self._json_cfg.items():
            Configuration._properties[name] = i
    def open_configuration(self):
        with open(self._fpath) as f:
            self._json_cfg = json.load(f)

    @property
    def properties(self):
        return self._properties
