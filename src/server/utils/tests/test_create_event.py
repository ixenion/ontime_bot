from src.server.utils.database_api.event_service import EventService
import pytest


@pytest.mark.asyncio
async def test_create_event():
    user_id = 1234567
    event_time = "12.11.2024 18:30:00"
    message = "Test event from external script"

    event_creator = EventService(db_name="events", db_user="postgres", db_pass="password", db_host="localhost", db_port="5432")

    result = await event_creator.create_event(user_id, message, event_time)

    if result:
        print("Event created successfully.")
    else:
        print("Failed to create event.")
