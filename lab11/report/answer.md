# Lab 11: Answer for questions
## 1.
Because **await** pauses execution of the current coroutine until the current task finishes. Since the loop does not move to the next iteration until the awaited task completes, tasks are executed one after another instead of overlapping in time.

## 2.
`asyncio.gather` schedules all coroutines at once and runs them concurrently within the event loop. Instead of waiting for each task one by one, it allows multiple tasks to progress during waiting periods (e.g., I/O), significantly improving performance for I/O-bound operations.

## 3. 
If any task raises an exception, `asyncio.gather` immediately propagates the error and cancels the whole operation. As a result, remaining tasks may not complete, and the program exits with a failure.

## 4.
A semaphore is used to limit the number of concurrently running tasks. This prevents launching too many tasks at once, which could overload system resources or external services, and allows controlled concurrency (e.g., max 5 tasks at a time).

## 5.
Async should not be used for CPU-bound tasks (heavy computations, image processing, ML training), because async does not run code in parallel on CPU cores. In such cases, multiprocessing or threading is more appropriate.