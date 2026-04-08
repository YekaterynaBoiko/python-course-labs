# Lab06: Python Object Model and Basic Object Behavior 
This folder contains **Lab 06** for the Python course.  
The goal of this lab is to understand the **Python object model** and how objects behave in Python. You will learn how attributes are stored, how to control object behavior, and how to implement **dunder methods**.  
  
## Python Version    
This lab was completed using **Python 3.10**.    
It is recommended to use the same version to avoid compatibility issues.  
  
## Lab Structures    
``` 
lab06/ 
|__README.md # Instructions and description of the lab      
|
|__requirements.txt # Required Python libraries (can be empty) 
|__ src/ # Folder containing all code files for the lab 
    |     
    |___lab06.py # Main code file for the lab 
|__report/    
    |___answer.md # Answers to lab questions  
 ```  
 ## Setup Instructions 
 1. **Clone the repository** (or navigate to this lab folder):    
``` 
git clone <repository_URL> 
cd <repository_folder>/lab06  
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
Run the  lab06 program:  
```  
python src/lab06.py  
```  
## Type Checking (Important)  
This project must pass **strict static type checking** using `mypy`.  
Run the following command:  
```  
python -m mypy --strict src/  
```  
or 
```
python -m mypy --strict src/lab06.py
```
The code should produce:  
*Success no issues found*  
  
## Lab description   
In this lab, we explore the Python object model and object behavior: 
- creating custom classes 
- working with object attributes 
- inspecting objects using __dict __
- modifying object state dynamically 
- implementing dunder methods: 
-- __str __ (user-friendly output)
-- __repr __ (developer-friendly output)
-- __eq __ (equality comparison)
-- __lt __ (ordering and sorting)
- integrating objects with Python built-in functions like *sort()*
- applying **type hints**
- ensuring correctness using **mypy --strict**
This lab demonstrates how Python treats objects internally and how to make them behave like built-in types.