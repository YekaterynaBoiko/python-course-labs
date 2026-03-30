# Lab05: Type Hints, Generics, Mypy
This folder contains **Lab 05** for the Python course.
The goal of this lab is to practice using **type hints** and to understand how static typing improves code reliability and clarity.

## Python Version  
This lab was completed using **Python 3.10**.  
It is recommended to use the same version to avoid compatibility issues.

## Lab Structures  
```  
lab05/  
|__README.md # Instructions and description of the lab  
|__requirements.txt # Required Python libraries (can be empty)  
|__ src/ # Folder containing all code files for the lab  
|     |___lab05.py # Main code file for the lab  
|__report/  
 |___answer.md # Answers to lab questions
 ```
 
 ## Setup Instructions  
1. **Clone the repository** (or navigate to this lab folder):  
```  
git clone <repository_URL>  
cd <repository_folder>/lab05
```  
2. Create a virtual environment (recommended):  
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
All required dependencies are listed in `requirements.txt`.
This project uses:
- `mypy` - for static type checking
Install dependencies using:
```
pip install -r requirements.txt
```

## How to Run
Run the  lab05 program:
```
python src/lab05.py
```
## Type Checking (Important)
This project must pass **strict static type checking** using `mypy`.
Run the following command:
```
python -m mypy --strict src/
```
The code should produce:
*Seccess no issues found*

## Lab description 
In this lab, we work with Python type hints and static typing. 
The following concepts are implemented and demonstrated: 
- basic type annotations for functions 
- typed collections (`list`, dict, tuple, etc.) 
- generics using TypeVar 
- function types using Callable 
- functions returning other functions 
- static type checking with mypy 
- strict typing discipline (`--strict` mode) 

This lab demonstrates how static typing improves code reliability, readability, and helps prevent runtime errors.