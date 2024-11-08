# -------------- #
# System imports #


# ------------------- #
# Third party imports #


# ------------- #
# Local imports #

from elogger        import Logger


# --------- #
# CONSTANTS #
# --------- #


# ------- #
# CLASSES #
# ------- #


class TestLoggerSingleton:

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


    def test_logger_init(self) -> None:
        """ Test that logger objects initialised without errors. """

        self.logger = Logger()
        assert self.logger is not None


    def test_logger_is_singleton(self) -> None:
        """ Test that there always be only one Logger instance."""

        logger_1 = Logger()
        logger_2 = Logger()
        assert id(logger_1) == id(logger_2)
