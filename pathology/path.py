import pathlib
import inspect


class Path(type(pathlib.Path())):
    @staticmethod
    def script_dir():
        return pathlib.Path(inspect.stack()[1].filename).parent.resolve()