# -------------- #
# System imports #

import asyncio
from datetime import datetime


# ------------------- #
# Third party imports #

import psycopg2
from psycopg2.extras import RealDictRow
from werkzeug.http import parse_dict_header

# ------------- #
# Local imports #

from .base import APIInterface


class CreateEvent(APIInterface):

    async def create_event(self, user_id: int, message: str, event_time: str) -> bool:
        """
        Add new event to DB

                Parameters:
                :param user_id: ID of the user;
                :param message: The message of the event. Example: "Консультация по ООП";
                :param event_time: The time in "DD.MM.YY, HH:MM:SS" format, when reminder must be sent to user. Example: "12.11.2024, 18:30:00";

                Returns:
                :return: A bool indicating success or failure;
        """
        try:
            parsed_event_time = datetime.strptime(event_time, "%d.%m.%Y %H:%M:%S")
            cmd = f"""
                  INSERT INTO Events (user_id, message, event_time, is_sent, created_at)
                  VALUES ({user_id}, '{message}', '{parsed_event_time}', FALSE, NOW());
            """
            await self.query(cmd)
            return True
        except Exception as e:
            print(f"Error while creating new event: {e}")
            return False



