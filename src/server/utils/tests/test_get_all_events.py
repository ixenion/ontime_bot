import pytest
from src.server.utils.database_api.event_service import EventService


@pytest.mark.asyncio
async def test_get_all_events():
    chat_id = 1234

    get_all_events = EventService(db_name="database", db_user="user", db_pass="user", db_host="localhost", db_port="5432")

    try:
        result = await get_all_events.get_all_events(chat_id)

        if result:
            print(f"Events gotten successfully.", result)
        else:
            print("No events")
    except Exception as ex:
        print(ex)
