
# Answer to Questions
## 1.
Type hints in Python are a way to explicitly specify the types of variables, function parameters, and return values. 
- They help detect errors before running the program using tools such as mypy. For example, they can detect when a value of type str is passed instead of int. 
- Type hints improve code readability, making it easier to understand. This helps when working with someone else’s code and reduces the risk of errors when modifying a program. 
- In development environments (IDEs) such as PyCharm, type hints are used for autocompletion, suggestions, and error checking. 
- Tools like mypy analyze the code without executing it and detect type-related errors.
- Type hints do not change the program’s behavior — they are only used for analysis, developer assistance, and improving code quality.

## 2.
The main difference between Any and T (TypeVar) is the following:  
- Any does not provide type checking, whereas TypeVar does.  
- TypeVar provides a high level of type safety, while Any has a low level of safety.  
- With Any, the type is not preserved, whereas TypeVar preserves the type throughout the code. 
- Any offers maximum flexibility, while TypeVar is flexible but with type control.

## 3. 
Callable[[int], int] is a function type annotation in Python that indicates the function takes one argument of type int and returns a value of type int. 

**mypy** checks whether a function matches this specified type. 

This helps prevent errors when passing functions as arguments.

## 4.
mypy --strict requires more type annotations because it performs full type checking. In strict mode, all functions, parameters, and variables must have explicit type annotations. 

Without annotations, mypy tries to infer (guess) types. However, in --strict mode this is not allowed, so types must be explicitly specified. 

This mode also enforces better code control, encouraging more structured and predictable code. Having more annotations provides greater control and helps reduce errors. 

For example, in strict mode, code without type annotations is not allowed.