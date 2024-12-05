# -------------- #
# System imports #


# ------------------- #
# Third party imports #


from psycopg2.extras import RealDictRow

# ------------- #
# Local imports #

from .base import APIInterface


class GetNextEvent(APIInterface):

    async def get_next_event(self, user_id: int) -> RealDictRow | None:
        """
        Get the next upcoming reminder for a user.

            Parameters:
            :param user_id: ID of the user.

            Returns:
            :return: The next event or None.
        """
        try:
            cmd = f"""
                   SELECT id, message, event_time
                   FROM Events
                   WHERE user_id = {user_id} AND is_sent = FALSE
                   ORDER BY event_time ASC
                   LIMIT 1;
            """
            response = await self.query(cmd)
            return response[0] if response else None
        except Exception as e:
            print(f"Error while getting next event: {e}")
            return False



