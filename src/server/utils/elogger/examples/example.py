# -------------- #
# System imports #


# ------------------- #
# Third party imports #


# ------------- #
# Local imports #

from elogger        import Logger


# Logger class is a singleton, don't hesitate to create objects :)
logger = Logger()
# But we can reset singleton by
#Logger._reset_instance()

# Demo of all logger levels.
logger.main.info(f"This is info")
logger.main.debug(f"This is debug")
logger.main.warning(f"This is warning")
logger.main.error(f"This is error")
logger.main.critical(f"This is critical")
# Also logger inherits from dict:
logger["main"].info(f"Also Im a dict!")


# Create another custom logger module with separate .log file
logger.create("mymodule")
logger.mymodule.info(f"This is info from 'mymodule'.")


# All logger modules supports stdout.
# By default every logger module has enabled stdout.
logger.mymodule.info(f"STDOUT enabled.")
logger.mymodule.stdout_mode(False)
logger.mymodule.info(f"STDOUT disabled.")
logger.mymodule.stdout_mode(True)
