# -------------- #
# System imports #


# ------------------- #
# Third party imports #

import psycopg2
from psycopg2.extras import RealDictRow


# ------------- #
# Local imports #

from .base import APIInterface


class GetAllEvents(APIInterface):

    async def get_all_events(self, user_id: int) -> list[RealDictRow] | None:
        """
        Gets all tasks from the database.
            Parameters:
            :param: user_id: ID of the user.

            Returns:
            :return: A list of events or None.
        """
        try:
            cmd = f"""
                    SELECT id, message, event_time
                    FROM Events
                    WHERE user_id = {user_id} AND is_sent = FALSE
                    ORDER BY event_time ASC;
                   """
            response = await self.query(cmd)
            return response
        except Exception as e:
            print(f"Error while getting events: {e}")
            return None
