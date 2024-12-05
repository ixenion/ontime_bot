import pytest
from src.server.utils.database_api.get_all_events import GetAllEvents


@pytest.mark.asyncio
async def test_get_all_events():
    user_id = 12345

    get_all_events = GetAllEvents(db_name="events", db_user="postgres", db_pass="password", db_host="localhost", db_port="5432")

    result = await get_all_events.get_all_events(user_id)

    if result:
        print(f"Events gotten successfully.", result)
    else:
        print("Failed to get events.")
