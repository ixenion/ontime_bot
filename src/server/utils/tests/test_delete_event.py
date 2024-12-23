from src.server.utils.database_api.event_service import EventService
import pytest


@pytest.mark.asyncio
async def test_delete_event():
    user_id = 1234
    event_id = 4

    event_creator = EventService(db_name="database", db_user="user", db_pass="user", db_host="localhost", db_port="5432")

    result = await event_creator.delete_event(user_id, event_id)

    if result:
        print("Event deleted successfully.")
    else:
        print("Failed to delete event.")

