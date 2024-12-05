import pytest
from src.server.utils.database_api.event_service import EventService


@pytest.mark.asyncio
async def test_mark_event_as_sent():
    event_id = 5

    event_marker = EventService(db_name="events", db_user="postgres", db_pass="password", db_host="localhost", db_port="5432")

    result = await event_marker.mark_event_as_sent(event_id)

    if result:
        print("Success")
    else:
        print("Failed")




