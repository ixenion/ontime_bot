from src.server.utils.database_api.event_service import EventService
import pytest


@pytest.mark.asyncio
async def test_create_user():
    username = "pavel"
    chat_id = 1234

    event_creator = EventService(db_name="database", db_user="user", db_pass="user", db_host="localhost", db_port="5432")

    result = await event_creator.create_user(username, chat_id)

    if result:
        print("User created successfully.")
    else:
        print("Failed to create user.")
