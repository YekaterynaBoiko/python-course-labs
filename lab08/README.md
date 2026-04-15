# Lab08: Iteration, Context Managers, and Descriptors  
This folder contains Lab 08 for the Python course.   
The goal of this lab is to understand how Python`s core protocols work by implementing a custom object that supports iteration, context management, and attribute validation through special methods.

## Python Version
This lab completed using Python 3.10. It is recommented to use the same version to avoid compatibility issues.

## Lab Structures
```
lab08/
|__README.md # Instructions and description of the lab
|
|__requirements.txt # Required Python libraries (can be empty)
|__src/ # Folder containing all code files for the lab
|  |___lab08.py # Main code file for the lab
|__report/
   |___answer.md # Answers to lab questions
   
 ```

## Setup Instructions
1. **Clone the repository** (or navigate to this lab folder):
```
git clone <repository_URL>
cd <repository_folder>/lab08
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

## How to Run
Run the lab08 program:
```
python src/lab08.py
```

## Type Checking (Important)
This project must pass **strict static type checking** using `mypy`. Run the following command:
```
python -m mypy --strict src/
```
The code should produce: *Success no issues found*

## Lab Structures
In this lab, you will build a student collection step by step while integrating key Python protocols. You will implement the iteration protocol to allow looping over objects, the context manager protocol to manage resources using the with statement, and descriptors to control and validate attribute access. This hands-on approach demonstrates how Python’s object model relies on special methods to define object behavior and extend functionality.