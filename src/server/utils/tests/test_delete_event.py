from src.server.utils.database_api.event_service import EventService
import pytest

DATABASE_URL = "postgresql://postgres:password@localhost:5432/events"


@pytest.mark.asyncio
async def test_delete_event():
    user_id = 12345
    event_id = 5

    event_creator = EventService(db_name="events", db_user="postgres", db_pass="password", db_host="localhost", db_port="5432")

    result = await event_creator.delete_event(user_id, event_id)

    if result:
        print("Event deleted successfully.")
    else:
        print("Failed to delete event.")

