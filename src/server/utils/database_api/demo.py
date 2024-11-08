# -------------- #
# System imports #

import asyncio
import datetime


# ------------------- #
# Third party imports #

import psycopg2
from psycopg2.extras    import RealDictRow


# ------------- #
# Local imports #

from .base       import APIInterface




###########
# CLASSES #
###########


class APIDemo(APIInterface):
    """
        Demo class.
    """

    async def test_get_users(self) -> list[RealDictRow]|None:
        """
        """

        cmd = f"SELECT * FROM USERS;"
        response = await self.query(cmd)
        return response
