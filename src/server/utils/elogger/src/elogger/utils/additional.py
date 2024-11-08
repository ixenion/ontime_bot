# -------------- #
# System imports #

from os                 import environ


# ------------------- #
# Third party imports #


# ------------- #
# Local imports #




# --------- #
# CONSTANTS #
# --------- #


# --------- #
# FUNCTIONS #

def env(key, type_, default=None) -> bool|int|str|None:
    """
        Get environment variable value.
        If there is no such variable in environment - use default.
        Supported value types: bool, int, str.
    """

    if key not in environ:
        return default

    val = environ[key]

    if type_ == str:
        return val
    elif type_ == bool:
        if val.lower() in ["1", "true", "yes", "y", "ok", "on"]:
            return True
        if val.lower() in ["0", "false", "no", "n", "nok", "off"]:
            return False
        raise ValueError(
            "Invalid environment variable '%s' (expected a boolean): '%s'" % (key, val)
        )
    elif type_ == int:
        try:
            return int(val)
        except ValueError:
            raise ValueError(
                "Invalid environment variable '%s' (expected an integer): '%s'" % (key, val)
            ) from None



# ------- #
# CLASSES #


