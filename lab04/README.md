# Lab04: Higher-Order Functions, map/filter, Decorators
This folder contains **Lab 04** for the Python course.
The goal of this lab is to practice using **higher_order functions** and understand how functions can be used to transform behavior.

## Python Version
This lab was completed using **Python 3.10**.
It is recommended to use the same version to avoid compatibility issues.

## Lab Structures
```
lab04/
|__README.md # Instructions and description of the lab
|__requirements.txt # Required Pyhton libraries (can be empty)
|__ src/ # Folder containing all code files for the lab
|     |___lab04.py # Main code file for the lab
|__report/
      |___answer.md # Answers to lab questions
```

## Setup Instructions
1. **Clone the repossitory** (or navigate to this lab folder):
```
git clone <repository_URL>
cd <repository_folder>/lab04
```
2. Create a virtual environment (recommended):
```
python -m venv venv
source venv/bin/activate # if you have Linux/macOS
venv\Scripts\activate # if you have Windows
```
3. Install dependencies (if any):
```
pip install -r requirements.txt
```
**For this lab, *requirements.txt* is empty since no external libraries are needed.**

## How to Run
To run the lab code:
```
python src/lab04.py
```

## Lab Description
In this lab, we work with higher-order functions and decorators in Python. In this lab, we have to: 
- use functions as arguments and return values (higher-order functions) 
- apply functional transformations using map and filter 
- compare map`/`filter with list comprehensions 
- implement decorators and show how they modify function behavior 
- create decorators with arguments 
- use decorators to implement simple caching mechanisms 

Overall, this lab helps to better understand functional programming concepts in Python and how to apply them in practice.