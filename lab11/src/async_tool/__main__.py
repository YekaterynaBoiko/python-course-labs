import asyncio
import argparse
import json
import logging
import sys
from typing import List


from .loader import load_tasks
from .runner import run_sequential, run_concurrent, run_limited
from .models import TaskItem, TaskResult

def setup_logging(level: str) -> None:
    logging.basicConfig(
        level = getattr(logging, level),
        format = "%(levelname)s: %(message)s",
    )


async def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("file")

    parser.add_argument(
        "--mode",
        choices=["sync", "async", "limited"],
        default = "sync",
    )

    parser.add_argument("--limit", type=int, default = 5)


    parser.add_argument(
        "--continue-on-error",
        action="store_true",
    )

    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="WARNING",
    )

    args = parser.parse_args()

    setup_logging(args.log_level)

    tasks: List[TaskItem]= load_tasks(args.file)

    try:
        if args.mode == "sync":
            result: List[TaskResult] = await run_sequential(
                tasks,
                args.continue_on_error
            )

        elif args.mode == "async":
            result = await run_concurrent(
                tasks,
                args.continue_on_error
            )

        elif args.mode == "limited":
            result = await run_limited(
                tasks,
                args.limit,
                args.continue_on_error,
            )
        print(json.dumps(result, indent=2))

    except Exception as e:
        logging.error(f"Program stopped: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())