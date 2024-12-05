# -------------- #
# System imports #


# ------------------- #
# Third party imports #


# ------------- #
# Local imports #

from .base import APIInterface


class MarkEventAsSent(APIInterface):

    async def mark_event_as_sent(self, event_id: int) -> bool:
        """
        Mark event as sent in DB after it was sent to user

                Parameters:
                :param event_id: ID of the event;

                Returns:
                :return: A bool indicating success or failure;
        """
        try:
            cmd = f"""
                  UPDATE Events
                  SET is_sent = TRUE
                  WHERE id = {event_id};
            """
            await self.query(cmd)
            return True
        except Exception as e:
            print(f"Error while marking event as sent: {e}")
            return False



