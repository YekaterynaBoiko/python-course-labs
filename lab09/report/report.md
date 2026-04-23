# Report: Refactoring and Improvement of Lab09 Project 
## 1. What was wrong in the original project 
The initial version of the project had several structural and design issues. 
The main problems were related to unclear package organization and inconsistent naming conventions. 
- The project structure was not clearly separated into modules with defined responsibilities. 
-  Function naming was inconsistent (mixed styles such as camelCase and snake_case).
- Some functions were not properly encapsulated as internal utilities. 
- Imports were initially unclear and not fully aligned with package-based structure. 
- The project lacked a clean and minimal dependency configuration. 

These issues made the code harder to read, maintain, and scale.  

## 2. What was improved 
During refactoring, the project was reorganized to follow proper Python package design principles. 
- The project was structured as a clear Python package (`report_tool`) with separated modules. 
- Responsibilities were divided into logical components: 
 -- numeric processing, 
 -- report formatting, 
 -- file operations. 
 - Functions were renamed to follow consistent Python naming conventions (snake_case). 
 - Internal helper functions were marked using underscore prefix to indicate restricted usage. 
 - A proper package entry point (`__main__.py`) was introduced. 
 - Imports were fixed to use relative package imports. 
 - The project was cleaned from unnecessary external dependencies. 

## 3. Why these changes matter 
These improvements significantly enhance the quality of the project: 
- **Readability**: consistent naming and structure make the code easier to understand. 
- **Usability**: clear entry point allows the project to be executed as a package.
- **Maintainability**: modular structure makes future changes easier and safer. 
- **Stability**: proper imports and separation reduce the risk of runtime errors. 
- **Scalability**: the project can now be extended without rewriting existing logic. 

Overall, the refactored version follows standard Python project organization practices and is easier to develop and maintain.