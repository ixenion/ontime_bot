from src.server.utils.database_api.event_service import EventService
import pytest


@pytest.mark.asyncio
async def test_create_event():
    chat_id = 1234
    event_time = "12.11.2024 18:45:00"
    message = "do smth else"

    event_creator = EventService(db_name="database", db_user="user", db_pass="user", db_host="localhost", db_port="5432")

    result = await event_creator.create_event(chat_id, message, event_time)

    if result:
        print("Event created successfully.")
    else:
        print("Failed to create event.")
