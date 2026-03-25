# Answer to Questions
## 1. 
A higher-order function is a function that works with other functions as objects.
The simplest example from the lab, in Task A, is passing a function as an object. The *apply* function takes a function *func* as an argument.
Such functions are useful:
- for proccesing lists
- in decorators
- and whenever you need to write simple, reusable code.

## 2.
Map is better to use for already defined functions and large data sets because it saves memory and clearly shows that a function is being applied.
On the other hand, lis comprehension is better for something simple, for example, when you need to filter elements.
The differnce between map and list comprehension is that with map you can pass any function,, while list comprehension works only within the list comprehension syntax.

## 3.
A decorator is a function that decorates another function: for example, it can count calls or modify the functions result.
It is used to:
- implement loggining, control, and counting of function calls
- make code cleaner and more reusable
- add behavior to a function without changing its code

For example, in Task E, we counted the number of times a function was called and printed the count each time it was called.

## 4.
The difference between a simple decorator and a decorator with arguments is that:
- A simple decorator takes only a function, while a decorator with parameters takes a function and additional arguments.
- A simple decorator is used for tasks like counting function calls or logging, whereas a decorator with parameters is used for adding prefixes or formating the functions results.

An example of simple decorator is Task E, where *call_counter* counts call without any extra parameters. 
An example of decorator with parameters is Task F, where *prefix("INFO")* passes the *text* argument to the decorator, which then adds the prefix to the functions result.

## 5.
Caching is useful because it saves time and computational resources by storing results, for example, of repeated function calls. 

This can be illustrated with Fibonacci numbers. If we need to calculate, for example, the 50th Fibonacci number, without caching the intermediate values would be recalculated many times. With caching, each unique value is **computed only once**, and all subsequent calls simply return the already computed result. This greatly saves time and memory. 

Another good example is the factorial of a large number, say 50. With caching, we can compute the result once and then use it repeatedly without recalculating. In short: caching allows programs to run much faster.[..](..)