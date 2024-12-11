import pytest
from src.server.utils.database_api.event_service import EventService


@pytest.mark.asyncio
async def test_get_event_by_time():
    user_id = 12345
    event_time = "2024-11-12 18:31:00"

    event_service = EventService(db_name="events", db_user="postgres", db_pass="password", db_host="localhost", db_port="5432")
    result = await event_service.get_event_by_time(user_id, event_time)

    assert result is None

