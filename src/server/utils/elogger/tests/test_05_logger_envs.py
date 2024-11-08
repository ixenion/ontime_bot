# -------------- #
# System imports #

from os             import environ, getenv
from shutil         import rmtree


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


class TestLoggerEnvs:

    def setup_method(self, method) -> None:
        """
            Fires before test. Usefull for test preps
            (create some objects etc)
        """
        
        # As Logger is Singleton and we need to test different Logger
        # instances between test_* files - need to reset Singleton.
        Logger._reset_instance()
        self.logger:None|Logger = None
        environ["LOG_FOLDER"] = "test_logs"

        self.LOG_FOLDER = getenv("LOG_FOLDER", default="")


    def teardown_method(self, method) -> None:
        """
            Fires after test was done. Usefull for test preps
            (delete some objects etc)
        """

        del self.logger
        del environ["LOG_FOLDER"]

        del self.LOG_FOLDER


    def test_logger_env_log_folder(self) -> None:
        """
            Here we try to make log entry to particular LOG_FOLDER
            specified by environment variable
            and confirm that it was created.

            parameters: None
        """

        # Create logger object (singleton)
        self.logger = Logger(folder_path=self.LOG_FOLDER)

        # Make one entry
        message = f"Test info message"
        self.logger.main.info(message)

        # Construct log path
        module_name:str = self.logger.main.module_name
        module_ext:Const.Extentions = self.logger.main.extention
        module = module_name + module_ext.value
        log_path = self.LOG_FOLDER + "/" + module

        # Read the log (will contain one line)
        with open(log_path, 'r') as f:
            content = f.read()

        assert message in content

        # Cleanup:
        # Remove 'env_log_folder' path
        rmtree(self.LOG_FOLDER)
