# -------------- #
# System imports #



# ------------------- #
# Third party imports #


# ------------- #
# Local imports #

from .base import APIInterface


class DeleteEvent(APIInterface):

    async def delete_event(self, user_id: int, event_id: int) -> bool:
        """
        Deletes a completed event from the database by its ID.

            Parameters:
            :param user_id: The user ID.
            :param event_id: The ID of the event to delete.

            Returns:
            :return: A success or failure boolean depending on if the event was deleted.
        """
        try:
            cmd = f"DELETE FROM Events WHERE id = {event_id} AND user_id = {user_id};"
            await self.query(cmd)
            return True
        except Exception as e:
            print(f"Error while deleting event: {e}")
            return False
