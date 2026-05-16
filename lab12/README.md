# Lab 12: Testing an Async CLI Tool
This lab is an asynchronous CLI tool that processes a list of tasks from a JSON file. Each task is processed using an async function process_item, which simulates delay and may fail based on input data. 

The lab demonstrates: 
- asynchronous programming in Python 
- CLI application development 
- unit testing async functions 
- black-box testing using subprocess

## Python Version  
This project is developed using **Python 3.11+**.

## Lab Structures  
```  
lab12/  
|__src/   
   |__async_tool/  
      |__ `__init__.py`     #package initialization 
      |__ `__main__.py` # CLI entry point 
      |__loader.py # JSON input loading 
      |__models.py # TaskItem, TaskResult, process_item 
      |_runner.py # execution logic (sync, async, limited)
|__test/
   |__test_process_item.py 
   |__test.cli.py
|__report/  
   |__answer.md
|__input.json # input file  
|__requirements.txt  
|__pytest.ini # pytest configuration
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
python -m venv venv source venv/bin/activate # if you have Linux/macOS 
venv\Scripts\activate # if you have Windows 
``` 
3. Install dependencies    
``` 
pip install -r requirements.txt 
```

## How to Run CLI
Run the tool with:
```
python -m src.async_tool input.json
```
### Options:
#### Default mode (sequential)
```
python -m src.async_tool input.json --mode sync
```
#### Async mode (concurrent execution)
```
python -m src.async_tool input.json --mode async
```
#### Limited concurrency
```
python -m src.async_tool input.json --mode limited --limit 5
```
#### Continue on error
```
python -m src.async_tool input.json --continue-on-error
```
## Running Tests
Install dependencies:
```
pip install pytest pytest-asyncio
```
Run tests:
```
pytest -v
```

## Test Strategy
### Unit tess:
- Directly test *process_item* 
- Validate success and failure cases 
- Check output structure 

### CLI tests 
- Use *subprocess.run* 
- Test full application as a black box 
- Validate: 
-- exit codes 
-- JSON output 
-- error handling 
-- execution modes

## Pytest Configuration
The lab uses *pytest.ini*:

    [pytest]
    asyncio_mode = auto
This enables async test execution.

## Status
All tests passing:
- Unit tests: 3/3
- CLI tests: 5/5