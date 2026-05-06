# Lab 11: Async Task Processing CLI Tool
In this lab, a CLI tool is implemented for processing a batch of tasks in different execution modes using `asyncio`.
The focus is on understanding:
- sequential vs concyrrent execution
- asyncio.gather usage
- concurrency control with Semaphore
- async error handling strategies

## Python Version
This project is developed using **Python 3.11+**.

## Lab Goal
The goal of this lab is to build a command-line application that processes tasks from a JSON file using different execution strategies without modifying core processing logic.

The application supports:
- sequential execution (sync)
- concurrent execution (async)
- limited concurrency execution (semaphore)
- configurable error handling
- configurable logging

## Lab Structures
```
lab11/
|__src/ 
   |__async_tool/
      |__ `__init__.py`     #package initialization
      |__ `__main__.py` # CLI entry point
      |__loader.py # JSON input loading
      |__models.py # TaskItem, TaskResult, process_item
      |_runner.py # execution logic (sync, async, limited)
|__report/
   |__answer.md
|__task.json # input file
|__requirements.txt
|__README.md
```
## Setup Instructions  
1. **Clone the repository** (or navigate to this lab folder):  
```  
git clone <repository_URL>  
cd <repository_folder>/lab11  
```  
2. Create a virtual environment (recommented):  
```  
python -m venv venv  
source venv/bin/activate # if you have Linux/macOS  
venv\Scripts\activate # if you have Windows  
```  
3. Install dependencies  
```  
pip install -r requirements.txt  
```  
  
## Requirements  
All required dependecies are listed in `requirements.txt`. This project uses:  
- `mypy` - for static type checking Install dependencies using:  
```  
pip install -r requirements.txt  
```

## How to Run]
Runn the program as a module from the project root:
### Sequential mode (sync)
```
python -m src.async_tool tasks.json --mode sync
```
### Async mode (concurrent execution)
```
python -m src.async_tool tasks.json --mode async
```
### Limited concurrency mode
```
python -m src.async_tool tasks.json --mode limited --limit 5
```

## Error Handling 
Default behavior:
- program stops on first error
- exit code &ne;

With flag:
```
--continue-on-error
```
- all tasks are executed
- failed tasks are returned in output

## Logging
Available levels:
- DEBUG
- INFO
- WARNING (default)
- ERROR

Example:
```
--log-level INFO
```

## Type Checking (mypy)
Run strict type check:
```
python -m mypy src/async_tool --strict
```
Expected result:

> Success: no issues found
