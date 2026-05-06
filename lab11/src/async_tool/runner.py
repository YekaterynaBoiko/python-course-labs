import asyncio
import logging
from typing import List
from .models import TaskItem, TaskResult, process_item


async def run_sequential(
        tasks: List[TaskItem],
        continue_on_error: bool
) -> List[TaskResult]:

    results: List[TaskResult] = []


    for task in tasks:
        logging.info(f"Start task {task['id']}")
        try:
            res = await process_item(task)
            logging.info(f"Done task {task['id']}")
            results.append(res)
        except Exception as e:
            logging.error(f"Error in task {task['id']}")

            if not continue_on_error:
                raise
            results.append({
                "id": task["id"],
                "status": "error",
                "message": str(e)
            })

    return results


async def run_concurrent(
        tasks: List[TaskItem],
        continue_on_error: bool
) -> List[TaskResult]:

    async def wrapper(task: TaskItem) -> TaskResult:
        logging.info(f"Start task {task['id']}")
        try:
            return await process_item(task)
        except Exception as e:
            logging.error(f"Error in task {task['id']}")

            if not continue_on_error:
                raise
            return {
                "id": task["id"],
                "status": "error",
                "message": str(e)
            }

    return list(await asyncio.gather(*(wrapper(t) for t in tasks)))


async def run_limited(
        tasks: List[TaskItem],
        limit: int,
        continue_on_error: bool
) -> List[TaskResult]:

    semaphore = asyncio.Semaphore(limit)

    async def wrapper(task: TaskItem) -> TaskResult:
        async with semaphore:
            logging.info(f"Start task {task['id']}")
            try:
                return await process_item(task)
            except Exception as e:
                logging.error(f"Error in task {task['id']}")

                if not continue_on_error:
                    raise
                return {
                    "id": task["id"],
                    "status": "error",
                    "message": str(e)
                }

    return list(await asyncio.gather(*(wrapper(t) for t in tasks)))