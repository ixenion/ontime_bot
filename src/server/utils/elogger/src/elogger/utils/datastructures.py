# -------------- #
# System imports #

from dataclasses        import dataclass
from enum               import Enum
from os                 import path as os_path, environ
from pathlib            import Path


# ------------------- #
# Third party imports #



# ------------- #
# Local imports #

from .additional     import env




# --------- #
# CONSTANTS #
# --------- #

LOG_FOLDER = env("LOG_FOLDER", str, None)
if LOG_FOLDER is None:
    # That means 'LOG_FOLDER' is not set in environment variable.
    LOG_FOLDER = Path(
            # Equals to "../../../../../logs/"
            # (1) ./ -> (2) elogger (src) -> (3) src -> \
            # (4) elogger (project) -> (5) external project
            Path(os_path.abspath(
                __file__)).parent.parent.parent.parent.parent.parent,
            "logs",
            )


# --------- #
# FUNCTIONS #


# ------- #
# CLASSES #

class Singleton(object):
    """
        Singleton to be inherited. The class who is inheriting
        become a singleton class which means - ony one object can
        be created from that class.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        """ Method responsible for new instance creation."""
        if cls._instance is None:
            cls._instance = \
                    super(Singleton, cls).__new__(cls)
        return cls._instance

    @classmethod
    def _reset_instance(cls):
        """ 
            !!! May lead to unpredictable results. Test use only !!!
            Reset the singleton instance.
        """

        cls._instance = None



class Const:
    """ Class containing constants."""

    @dataclass
    class Compression:
        ZIP:str = "zip"
        GZ:str  = "gz"
        BZ2:str = "bz2"
        XZ:str  = "xz"

    @dataclass
    class Level:
        TRACE:int   = 5
        DEBUG:int   = 10
        INFO:int    = 20
        SUCCESS:int = 25
        WARNING:int = 30
        ERROR:int   = 40
        CRITICAL:int    = 50

    class Extentions(Enum):
        NONE:str    = ""
        LOG:str     = ".log"
        TXT:str     = ".txt"
