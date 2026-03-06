# LAB01: Names & Objects (binding), mutability, copy, GC (CPython)

## Short description of the lab
The purpose of this lab is to demonstrate in Pyhon, names are bindings to objects, not variables in the traditional sense.
The following concepts are explored in the lab:
- rebinding and mutation
- passing arguments to functions
- copy semantics (shallow and deep copy)
- reference counting and garbage collection in CPython

## Environment Setup 
Make sure that Python 3.10 is installed on your system.

Create a virtual environment:
python -m venv .venv

Activate the virtual environment:
.venv\Scripts\activate

## Comand to run the program
To run the program, use the following comand:
python src/lab01.py

## Descripion of Program Output
The program prints six sections(A-F). Each section demonstrates a specific concept related to how Python works with names and objects.
- **A - Binding / Rebinding** 
  Demonstrates that names in Python are bindings to objects and shows what happens when a name is rebound to another object.
- **B - Mutation vs Rebinding**
  Shows the difference between modifying an existing object(mutation) and assigning a name to a new object(rebinding).
- **C - Function Arguments**
  Demonstrates how function arguments create new bindings and how mutation inside a function can affect the original object.
- **D - Default Argument Behavior**
  Shows how mutable default arguments can lead to unexpected behavior because the same object is reused between function calls.
- **E - Copy Semantics**
  Demonstrates the difference between shallow copy and deep copy, especially when working with nested objects.
- **F - Reference Counting / Garbage Collection**
  Shows how reference counting works in CPython and how the number of reference to an object can change.