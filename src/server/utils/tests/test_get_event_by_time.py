import pytest
from src.server.utils.database_api.event_service import EventService


@pytest.mark.asyncio
async def test_get_event_by_time():
    chat_id = 1234
    event_time = "2024-11-12 18:45:00"

    event_service = EventService(db_name="database", db_user="user", db_pass="user", db_host="localhost", db_port="5432")

    try:
        result = await event_service.get_event_by_time(chat_id, event_time)

        if result:
            print(f"Events gotten successfully.", result)
        else:
            print("No events")
    except Exception as ex:
        print(ex)


