# -------------- #
# System imports #

from datetime           import time, timedelta
from pathlib            import Path
from sys                import stdout
from typing             import Callable, Coroutine


# ------------------- #
# Third party imports #

from loguru._logger     import Logger as _Logger, Core, _defaults
from loguru._handler    import Handler


# ------------- #
# Local imports #

from elogger.utils.datastructures    import LOG_FOLDER, Singleton, Const
from elogger.utils.exceptions        import LoggerAttributeError




# --------- #
# CONSTANTS #
# --------- #



# ------- #
# CLASSES #
# ------- #


class LoggerUnit(_Logger):
    """
        An object to dispatch logging messages to configured handlers.
    """

    def __init__(self,
                 module_name:str, extention:Const.Extentions,
                 stdout_mode:bool=True):
        super().__init__(
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

        self.module_name:str = module_name
        self.extention:Const.Extentions = extention
        # To manage enable/disable stdout mode.
        self.stdout_sink_enabled:bool = False
        self.stdout_sink_handler_id:int|None = None

        if stdout_mode:
            self.stdout_mode(enable=True)


    def stdout_mode(self, enable:bool) -> int|None:
        """
            Enables | Disables STDOUT mode.
            If enable=True - LoggerInstance (aka module) will also
            print to STDOUT. enable=False - disables it.
            Returns handler_id which returned by _Logger.add method.
        """

        # Check do we need to enabled or disabled state.
        if enable:
            # Enable stdout sink
            if self.stdout_sink_enabled:
                # It's already enabled - return handler_id
                handler_id = self.stdout_sink_handler_id
            else:
                # It's disabled - enable and return handler_id
                handler_id = self._stdout_sink_enable()
        else:
            # Disable stdout sink
            if not self.stdout_sink_enabled:
                # It's already disabled - return handler_id = None
                handler_id = None
            else:
                # It's enabled - disable and return handler_id = None
                handler_id = self._stdout_sink_disable()

        self.stdout_sink_handler_id = handler_id
        return handler_id


    def _stdout_sink_enable(self) -> int:
        """ Enables LoggerInstance STDOUT."""

        handler_id = self.add(
                sink=stdout,
                level="TRACE",
                format=f"[{self.module_name.upper()}] " + \
                        "{time} {level} {message}",
                )
        self.stdout_sink_enabled = True
        return handler_id

    def _stdout_sink_disable(self) -> None:
        """ Disables LoggerInstance STDOUT."""

        if self.stdout_sink_handler_id is None:
            # Oops, that should not be happen.
            # Just lets assume that stdout sink wasnt started.
            pass
        else:
            # We have self.stdout_sink_handler_id which is int
            # and not None. Lets remove this sink
            self.remove(self.stdout_sink_handler_id)

        self.stdout_sink_enabled = False
        return




class Logger(Singleton, dict):
    """
        This class creates multiple instances of Logger class,
        So that user have opportunity to write multiple logs
        in different files.
        Useful if you want to separate log streams withing one programm.
    """
    

    def __init__(self, folder_path:Path|str=LOG_FOLDER) -> None:
        """
            Parameters:

            - folder_path:  Folder where Logger to write ALL logs
                            from all modules.
        """

        self.folder:Path|str = folder_path
        self.logs_extention:Const.Extentions = Const.Extentions.LOG
        #TODO: make use handlers
        # self.handlers:dict[str,str] = {}
        

        # Create default (named main) LoggerInstance module.
        self._default_module_name:str = "main"
        self._default_module_ext:Const.Extentions = Const.Extentions.LOG
        self.create(module_name=self._default_module_name,
                    extention=self._default_module_ext)


    def __getattr__(self, module_name:str) -> LoggerUnit:
        """
            Checks if there is attribute with a given name.
            If yes - return it, no - raises Exception.
        """

        if hasattr(self, module_name):
            return getattr(self, module_name)
            # super().__getattr__(self, module_name)
        # If we here - there is no attribute with a given name,
        raise LoggerAttributeError(attr_name=module_name)
    

    def create(
            self,
            module_name:str,
            stdout_mode:bool=True,
            sink:str|Path|Callable|Coroutine|Handler|None=None,
            format:str|Callable="{time} {level} {message}",
            rotation:str|int|time|timedelta|Callable="10 MB",
            # Keep logs for 7 days
            retention:str|int|timedelta|Callable="7 days",
            # Log files will be compressed in zip format
            compression:str|Callable|Const.Compression=\
                    Const.Compression.ZIP,
            level:int|str|Const.Level=Const.Level.TRACE,
            extention:Const.Extentions = Const.Extentions.LOG,
            filter=_defaults.LOGURU_FILTER,
            colorize=_defaults.LOGURU_COLORIZE,
            serialize=_defaults.LOGURU_SERIALIZE,
            backtrace=_defaults.LOGURU_BACKTRACE,
            diagnose=_defaults.LOGURU_DIAGNOSE,
            enqueue=_defaults.LOGURU_ENQUEUE,
            context=_defaults.LOGURU_CONTEXT,
            catch=_defaults.LOGURU_CATCH,
            **kwargs,
            ) -> LoggerUnit:
        """
            Creates new LoggerInstance modules.

            Parameters: just read 'loguru._logger.Logger.add' method
            (it's hundreeds of lines which I dont want to copy here)
            
            Usage example:

            logger = Logger()
            logger.create('mymodule')
            # Now you can address it to make logs:
            logger.mymodule.info(f"Im alive")
            # And log files will be stored in
            # /self.log_path/mymodule.log
        """

        if sink is None:
            sink = Path(self.folder, module_name + extention.value)

        # Create Logger:
        logger = LoggerUnit(module_name, extention, stdout_mode)
        logger.add(
            sink=sink, format=format, rotation=rotation,
            retention=retention, compression=compression, level=level,
            filter=filter, colorize=colorize, serialize=serialize,
            backtrace=backtrace, diagnose=diagnose,
            enqueue=enqueue, context=context, catch=catch, 
            **kwargs,
            )

        setattr(self, module_name, logger)
        # Also add dict key:val pair
        self[module_name] = logger

        return logger
