# Lab07: Behavior, Protocols, ABC, Dataclasses, Slots 
This folder contains Lab 07 for the Python course. 
The goal of this lab is to explore different ways of defining and implementing behavior in Python using a serializable object. You will learn how Python relies on behavior rather than inheritance by applying concepts such as duck typing, Protocols, dataclasses, slots, and Abstract Base Classes (ABC). The lab also aims to demonstrate the differences between these approaches in terms of flexibility, structure, and type safety.

## Python Version 
This lab completed using Python 3.10. It id recommended to use the same version to avoid compatibility issues.

## Lab Structures
```
lab07/
|__README.md # Instructions and description of the lab
|
|__requirements.txt # Required Pyrhon libraries (can be empty)
|__src/ # Folder containing all code files for the lab
   |___lab07.py # Main code file for the lab
|__report/
   |___answer.md # Answers to lab questions
 ```

## Setup Instructions
1. **Clone the repository** (or navigate to this lab folder):
```
git clone <repository_URL>
cd <repository_folder>/lab07
```
2. Create a virtual environment (recommented);
```
python -m venv venv
source venv/bin/activate # if you have Linux/macOS
venv\Scripts\activate # if you have Windows
```
3. Install dependencies:
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
Run the lab07 program:
```
python src/lab07.py
```

## Type Checking (Important)
This project must pass **strict static type checking** using `mypy`.
Run the following command:
```
python -m mypy --strict src/
```
or
```
python -m mypy --strict src/lab07.py
```
The code should produce:
*Successs no issues found*

## Lab description
In this lab, you will implement a serializable object using different approaches in Python, including duck typing, Protocols, dataclasses, slots, and Abstract Base Classes (ABC). You will compare these methods to understand how object behavior can be defined in multiple ways and how Python’s typing system works in practice.
