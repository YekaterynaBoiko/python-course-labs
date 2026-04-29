# Lab 10: Turning a Python Package into a CLI Tool
This project is Lab 10 for th Python course.

In this lab, an existing report generation system is extended into a fully functional command-line utility. The focus is on turning a modular Pyrhon package into a real-world CLI tool with file-based input/output, configurable logging, and multiple output formats.

## Python Version 
This project is developed using **Python 3.10**.

## Lab Goal
The main goal of this lab is to extend an existing codebase ('report_tool') into a flexible command-line application that can be used without modifying the source code.

The application now suppors:
- external input files
- configurable output files
- multiple output formats
- logging control via CLI arguments


## Lab Structures
```
lab10/
|__src/
   |__report_tool/
      |__ `__init__.py` # file defines the public interface of report_tool package
      |__`__main__.py`  # CLI entry point
      |__ numbers.py # parsing and analysis logic
      |__ textstuff.py # report formatting
      |__ saveit.py # file operations
|
| __report/
    |__report.md  # answers to questions
|__data.txt # input data file 
|__result.txt # generated output file
|__requirements.txt
|__README.md
```

## Features
The tool provides the following functionality: 
- Reads numeric data from external files 
- Parses and cleans input data 
- Performs statistical analysis: 
 --minimum value 
 -- maximum value 
 -- sum 
 -- count 
 -- mean 
 - Generates reports in multiple formats: -
 --text — human-readable report 
 -- json — structured data format 
 - Saves results to an output file 
 - Logs execution steps using configurable log levels

## Requirements   
This project does not require externall libraries.  
All functionality is implemented using Python standart library.  
  
If needed, install dependencies:  
```  
pip install -r requirements.txt  
```

## How to Run
The tool is executed as a Python **module** from the project root:
### Text format
```
python -m src.report_tool --input data.txt --out result.txt --format text --log-level INFO
```
JSON format:
```
python -m src.report_tool --input daa.txt --out result.json --format json --log-level INFO
```

## Notes
- The project is implemented as a modular Python package (report_tool)
- `__main__.py ` serves as the CLI entry point 
- Business logic is separated into independent modules
- No external libraries are required
- The tool is designet to be reusable and extensible