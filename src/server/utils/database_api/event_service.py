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


class EventService(APIInterface):

    async def create_event(self, chat_id: int, message: str, event_time: str) -> bool:
        """
        Add new event to DB

                Parameters:
                :param chat_id: ID of the user in telegram chat;
                :param message: The message of the event. Example: "Консультация по ООП";
                :param event_time: The time in "DD.MM.YY, HH:MM:SS" format, when reminder must be sent to user. Example: "12.11.2024, 18:30:00";

                Returns:
                :return: A bool indicating success or failure;
        """
        try:
            parsed_event_time = datetime.strptime(event_time, "%d.%m.%Y %H:%M:%S")
            cmd_user_id = f"""
                   SELECT id FROM users 
                   WHERE chat_id = '{chat_id}';
            """
            user_id = await self.query(cmd_user_id)
            if not user_id:
                print(f"User with chat_id {chat_id} not found.")
                return False
            else:
                user_id = user_id[0]["id"]

            cmd = f"""
                  INSERT INTO events (user_id, message, event_time, is_sent, created_at, is_deleted)
                  VALUES ({user_id}, '{message}', '{parsed_event_time}', FALSE, NOW(), FALSE);
            """
            await self.query(cmd)
            return True
        except Exception as e:
            print(f"Error while creating new event: {e}")
            return False

    async def get_all_events(self, chat_id: int) -> list[RealDictRow] | None:
        """
        Gets all tasks from the database.
            Parameters:
            :param: user_id: ID of the user.

            Returns:
            :return: A list of events or None.
        """
        try:
            cmd = f"""
                    SELECT events.event_id, events.message, events.event_time
                    FROM events
                    JOIN users ON users.id = events.user_id 
                    WHERE users.chat_id = '{chat_id}' AND events.is_sent = FALSE
                    ORDER BY events.event_time ASC;
                   """
            response = await self.query(cmd)
            return response
        except Exception as e:
            print(f"Error while getting events: {e}")
            return None

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
                      FROM events
                      WHERE user_id = {user_id} AND is_sent = FALSE
                      ORDER BY event_time ASC
                      LIMIT 1;
               """
            response = await self.query(cmd)
            return response[0] if response else None
        except Exception as e:
            print(f"Error while getting next event: {e}")
            return False

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
                  UPDATE events
                  SET is_sent = TRUE
                  WHERE id = {event_id};
            """
            await self.query(cmd)
            return True
        except Exception as e:
            print(f"Error while marking event as sent: {e}")
            return False

    async def delete_event(self, chat_id: int, event_id: int) -> bool:
        """
        Deletes a completed event from the database by its ID.

            Parameters:
            :param chat_id: ID of the user in telegram chat;
            :param event_id: The ID of the event to delete.

            Returns:
            :return: A success or failure boolean depending on if the event was deleted.
        """
        try:
            cmd_user_id = f"""
                            SELECT id FROM users 
                            WHERE chat_id = '{chat_id}';
            """
            user_id = await self.query(cmd_user_id)
            if not user_id:
                print(f"User with chat_id {chat_id} not found.")
                return False
            else:
                user_id = user_id[0]["id"]

            cmd = f"DELETE FROM events WHERE event_id = {event_id} AND user_id = {user_id};"
            await self.query(cmd)
            return True
        except Exception as e:
            print(f"Error while deleting event: {e}")
            return False

    async def get_event_by_time(self, chat_id: int, event_time: str) -> list[RealDictRow] | None:
        """
        Get all events witch should be sent by exact time.

            Parameters:
            :param chat_id: ID of the user in telegram chat.
            :param event_time: Time of the event.

            Returns:
            :return: The list of events or None.
        """
        try:
            cmd = f"""
                   SELECT events.event_id, events.message, events.event_time
                   FROM events
                   JOIN users ON users.id = events.user_id 
                   WHERE users.chat_id = '{chat_id}' AND events.is_sent = FALSE AND events.event_time = '{event_time}'
            """

            result = await self.query(cmd)
            return result if result else None
        except Exception as e:
            print(f"Error while getting event: {e}")

    #USERS METHODS

    async def create_user(self, username: str, chat_id: int) -> bool:
        """
        Add new user to DB

                Parameters:
                :param username: The message of the event. Example: "Консультация по ООП";
                :param chat_id: ID of user in Telegram system;

                Returns:
                :return: A bool indicating success or failure;
        """
        try:
            cmd = f"""
                  INSERT INTO users (username, chat_id)
                  VALUES ('{username}', {chat_id});
            """
            await self.query(cmd)
            return True
        except Exception as e:
            print(f"Error while creating new user: {e}")
            return False
