## Description
elogger - shor for extended logger. The core of the project is the best open-source logging library - loguru:
https://github.com/Delgan/loguru

The problem with loguru is that it's not simple to create new logger object to avoid sinks mixing.
For example when trying to write several separate log files with different log content we have to create new logger object like so:

```python
from loguru._logger     import Logger, Core

new_logger = _Logger(
        core=Core(),
        exception=None,
        depth=0,
        record=False,
        lazy=False,
        colors=True,
        raw=False,
        capture=True,
        patchers=[],
        extra={},
    )

# Add sinks
new_logger.add(...)
```

So elogger came to simplify this problem.


## Installation

Install the source as python package

```shell
git clone https://github.com/ixenion/elogger
cd elogger
pip install -e .

# Set LOG_FOLDER folder
export LOG_FOLDER="../path/to/logs"
# Otherwise will use default: "../" - one dir above from source.

# Delete env var if needed:
# unset LOG_FOLDER
```


## Usage:

```python
# -------------- #
# System imports #

# ------------------- #
# Third party imports #

from elogger        import Logger

# ------------- #
# Local imports #


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
```

When STDOUT for logger module is enabled, output be like:

```shell
[MAIN] 2024-09-05T23:40:37.155001+0300 INFO This is info
[MAIN] 2024-09-05T23:40:37.155175+0300 DEBUG This is debug
[MAIN] 2024-09-05T23:40:37.155266+0300 WARNING This is warning
[MAIN] 2024-09-05T23:40:37.155341+0300 ERROR This is error
[MAIN] 2024-09-05T23:40:37.155411+0300 CRITICAL This is critical
[MAIN] 2024-09-05T23:40:37.155481+0300 INFO Also Im a dict!
[MYMODULE] 2024-09-05T23:40:37.167594+0300 INFO This is info from 'mymodule'.
[MYMODULE] 2024-09-05T23:40:37.167703+0300 INFO STDOUT enabled.
```

For more docs address loguru project
https://github.com/Delgan/loguru
