import asyncio
from typing import List
from .models import TaskItem, TaskResult, process_item


async def run_sequential(tasks: List[TaskItem], continue_on_error: bool) -> List[TaskResult]:
    results = []

    for task in tasks:
        try:
            res = await process_item(task)
        except Exception as e:
            if continue_on_error:
                results.append({
                    "id": task["id"],
                    "status": "error",
                    "message": str(e),
                })
                continue
            raise
        results.append(res)

    return results


async def run_concurrent(tasks: List[TaskItem], continue_on_error: bool) -> List[TaskResult]:
    results = []

    async def handle(task):
        try:
            return await process_item(task)
        except Exception as e:
            if continue_on_error:
                return {
                    "id": task["id"],
                    "status": "error",
                    "message": str(e),
                }
            raise

    results = await asyncio.gather(*(handle(t) for t in tasks))
    return results


async def run_limited(tasks: List[TaskItem], limit: int, continue_on_error: bool) -> List[TaskResult]:
    semaphore = asyncio.Semaphore(limit)
    results = []

    async def handle(task):
        async with semaphore:
            try:
                return await process_item(task)
            except Exception as e:
                if continue_on_error:
                    return {
                        "id": task["id"],
                        "status": "error",
                        "message": str(e),
                    }
                raise

    results = await asyncio.gather(*(handle(t) for t in tasks))
    return results