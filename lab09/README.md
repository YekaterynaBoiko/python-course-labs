# Lab09: Modules, Packages, and File Handling 

This folder contains Lab 09 for the Python course. 
The goal of this lab is to understand how Python packages work and how to organize code into modules. The project also demonstrates working with data processing, formatting, and file input/output operations. 

## Python Version 
This lab is completed using Python 3.10. 
It is recommended to use the same version to avoid compatibility issues. 

 ## Lab Structure
 ```
 lab09/
 |__README.md  # Instructions and description of the lab
 |__requiremens.txt  # Required Python libraries (no external dependencies)
 |
 |__src/ # Folder containing all source code
     |__report_tool/ # Python package
        |__main.py # Entry point of the program
        |__numbers.py # Parsing and analyzing numbers
        |__textstuff.py # Report formatting
        |__saveit.py # File saving and reading
        |__init.py 
 |__report/ # Additional materials or task descrition
    |__report.md
 ```
## Setup Instructions
### 1. Open the project folder
Navigate to the lab directory:
```
cd lab09
```
Or open it directly in:
- PyCharm -> File -> Open
- VS Code -> File -> Open Folder

### 2. Open terminal in project directory
Make sure you are in:
```
lab09/src
```
If not, run:
```bash
cd src
```

## Requirements 
This project does not require externall libraries.
All functionality is implemented using Python standart library.

If needed, install dependencies:
```
pip install -r requirements.txt
```

## How to Run
Run the program using module execution:
```
python -m report_tool
```

## Program Description
In this lab, a simple report generation system is implemented. The program: 
- Parses numeric data from a text input 
- Analyzes numbers (count, sum, min, max, mean) 
- Sorts the data 
- Generates a formatted report 
- Saves the report into a ***.txt*** file 
- Reads the saved file and displays its content

## Notes 
- The project is structured as a Python package (report_tool) 
- `__main__.py` is the entry point of the application 
- Each module has a separate responsibility: 
 --- **`numbers.py`** → data processing 
 --- **`textstuff.py`** → formatting 
 --- **`saveit.py`** → file operations 
 - Output file is created automatically during execution