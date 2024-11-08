# -------------- #
# System imports #

import asyncio


# ------------------- #
# Third party imports #

from elogger        import Logger

# ------------- #
# Local imports #

# from .db_api         import Database
from .database_api       import Database


# --------- #
# CONSTANTS #


# ------- #
# OBJECTS #

# Create logger object to make and store logs.
logger = Logger()
logger.create(module_name="server")
logger.server.info("Logger module initialised.")

# Create database object to communicate with postgres
database = Database()



# --------- #
# FUNCTIONS #


# ------- #
# CLASSES #


# ---- #
# MAIN #
