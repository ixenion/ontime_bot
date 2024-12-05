import pytest
from src.server.utils.database_api.get_next_event import GetNextEvent


@pytest.mark.asyncio
async def test_get_next_event():
    user_id = 12345

    next_event_getter = GetNextEvent(db_name="events", db_user="postgres", db_pass="password", db_host="localhost", db_port="5432")

    result = await next_event_getter.get_next_event(user_id)

    if result:
        print("Next event gotten successfully", result)
    else:
        print("Next event gotten failed")