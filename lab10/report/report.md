# Report Lab 10:
## 1.
In this lab, the existing `report_tool` project was extended with several new capabilities: 
### CLI interface 
The tool was transformed into a command-line application using `argparse.` It now accepts parameters at runtime instead of using hardcoded values. 
### File input/output 
The program now: 
- reads numeric data from an external input file 
- writes processed results to a specified output file 

This makes the tool reusable for different datasets without changing the code. 
### JSON output support 
In addition to text reports, the tool now supports: 
- `text` format — human-readable report 
- `json` format — structured machine-readable output 

Both formats are generated from the same analysis result. 
### Logging system 
The application uses Python’s `logging` module to track execution steps, including: 
- reading input 
- parsing data 
- analyzing numbers 
- generating report 
- saving output 

Logging level can be controlled via CLI arguments.

## 2.
Previously, the tool worked as a simple script with: 
- fixed input data 
- direct execution 
- limited flexibility 

After improvements, it became a fully functional CLI tool. 
### Before: 
- Hardcoded execution flow 
- No external input handling 
- No configuration options 

### After: 
- Fully command-line driven execution 
- Flexible input and output file handling 
- Support for multiple output formats 
- Configurable logging system 
- Modular and reusable structure

## 3. 
These improvements make the tool closer to real-world applications. 
### CLI usability and automation 
A command-line interface allows the tool to be: 
- easily integrated into scripts 
- used in automated workflows 
- executed with different parameters without code changes 

### JSON output 
JSON format is important because: 
- it is machine-readable 
- it can be easily used by other programs or APIs 
- it supports data exchange between systems 

### Logging 
Logging improves: 
- debugging and error tracking 
- transparency of execution flow 
- monitoring of each processing stage