# -------------- #
# System imports #


# ------------------- #
# Third party imports #



# ------------- #
# Local imports #

from elogger        import Logger
from elogger.utils.datastructures    import Const


# --------- #
# CONSTANTS #
# --------- #


# ------- #
# CLASSES #
# ------- #


class TestCustomLoggerModule:

    def setup_method(self, method) -> None:
        """
            Fires before test. Usefull for test preps
            (create some objects etc)
        """
        
        # As Logger is Singleton and we need to test different Logger
        # instances between test_* files - need to reset Singleton.
        Logger._reset_instance()
        self.logger:None|Logger = None


    def teardown_method(self, method) -> None:
        """
            Fires after test was done. Usefull for test preps
            (delete some objects etc)
        """

        del self.logger


    def test_logger_custom_sink(self, tmp_path) -> None:
        """
            Here we try to make log entry and confirm that it was created.

            parameters:

            - tmp_path:     Is a fixture. Points to the root dir:
                            log_system.
        """

        # Create logger object (singleton)
        self.logger = Logger(folder_path=tmp_path)
        # Create new logger module
        self.logger.create("autotest")
        # Make one entry
        message = f"Test info message"
        self.logger.autotest.info(message)

        # Construct log path
        module_name:str = self.logger.autotest.module_name
        module_ext:Const.Extentions = self.logger.autotest.extention
        module = module_name + module_ext.value
        log_path = tmp_path / module

        # Read the log (will contain one line)
        with open(log_path, 'r') as f:
            content = f.read()

        assert message in content


    def test_logger_custom_levels(self, tmp_path) -> None:
        """
            Here we try to make several log entries and check their level.

            parameters:

            - tmp_path:     Is a fixture. Points to the root dir:
                            log_system.
        """

        # Create logger object (singleton)
        Logger._reset_instance()
        self.logger = Logger(folder_path=tmp_path)
        self.logger.create("autotest")

        message = f"Test info message"
        # Write all sorts of levels log
        self.logger.autotest.trace(message)
        self.logger.autotest.debug(message)
        self.logger.autotest.info(message)
        self.logger.autotest.info(message)
        self.logger.autotest.success(message)
        self.logger.autotest.warning(message)
        self.logger.autotest.error(message)
        self.logger.autotest.critical(message)

        # Construct log path
        module_name:str = self.logger.autotest.module_name
        module_ext:Const.Extentions = self.logger.autotest.extention
        module = module_name + module_ext.value
        log_path = tmp_path / module
        
        # Read the log (will contain one line)
        with open(log_path, 'r') as f:
            content = f.read()

        success = "TRACE" and "DEBUG" and "INFO" and "SUCCESS" and \
                "WARNING" and "ERROR" and "CRITICAL" in content

        assert success == True

    
    #TODO: Make proper tests.
    def test_logger_custom_stdout(self, tmp_path, caplog) -> None:
        """
            Here we try to make log entry and catch STDOUT.

            parameters:

            - tmp_path:     Is a fixture. Points to the root dir:
                            log_system.
        """

        # Create logger object (singleton)
        self.logger = Logger(folder_path=tmp_path)
        self.logger = Logger(folder_path=tmp_path)
        self.logger.create("autotest")
        # Set up (enable) STDOUT for default module
        # (it enabled by default btw)
        self.logger.autotest.stdout_mode(enable=True)
        
        # Write log
        magic_handler_id = \
                self.logger.autotest.add(sink=caplog.handler, level=0)
        
        message = f"Test info message"
        self.logger.autotest.info(message)
        tmp = caplog.text

        assert message in tmp
        
        # Disable stdout.
        self.logger.autotest.stdout_mode(enable=False)
        # Next line should not be, otherwise we dont test stdout.
        self.logger.autotest.remove(magic_handler_id)

        
        message = f"Test info message - no stdout"
        self.logger.autotest.info(message)
        tmp = caplog.text

        assert message not in tmp

