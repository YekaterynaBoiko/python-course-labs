import pytest
from src.async_tool.models import process_item, TaskItem


@pytest.mark.asyncio
async def test_process_item_success():
    item: TaskItem = {
        "id": 1,
        "delay": 0,
        "good": True,
    }

    result = await process_item(item)

    assert result == {
        "id": 1,
        "status": "done",
        "message": "",
    }


@pytest.mark.asyncio
async def test_process_item_failure():
    item: TaskItem = {
        "id": 2,
        "delay": 0,
        "good": False,
    }

    with pytest.raises(ValueError):
        await process_item(item)


@pytest.mark.asyncio
async def test_process_item_structure():
    item: TaskItem = {
        "id": 3,
        "delay": 0,
        "good": True,
    }

    result = await process_item(item)

    assert set(result.keys()) == {"id", "status", "message"}