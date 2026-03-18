## Task A - Thruthiness
In Python, objects that contain nothing are considered False.
For example, an empty list [] is evaluated as False
because it has no elements, while [1] is True because 
it contains one element and is not empty.
None is also False because it represents the absence of a value. 
In Python, it is treated as False for this  reason.


## Task B - Identity vs Equality
In the first case, it returns False becauese we create
two separate lists in memory. Although their values
are the same, they are different objects,
so is checks the memory identity. On the other hand, == checks
the contents of the lists and returns True because thier
values are equal. 
In the second case, we have two identical objects: c
is just a reference to value a. Therefore, values: a is c returns True
because they are the same objects in memory. And 
== also returns True, as i the first case, because 
their contents are equal.
In the third case, is returns True because for
immutable types(int or str) Python may reuse small
objects in memory. Therefore, x_example and y_example
refer to the same object. If we used a larger number,
like a 1000, "is" would return False, because 
Python does not reuse memory for large numbers.
From these three cases, we can draw a general 
conclusion: == checks whether the contens(values)
are equal, while "is" checks whether the two variables \
refer to the same object in memory.


## Task D - Pattern Matching
match is convenient because it allows us to check 
the structure of data and extract values at the same 
time. It is more convenient than writing multiple
if/elif statements, where we would need to manually
check indices. With match, the structures of the data 
is clearly visible, and variables can be extracted
automatically. This makes the code cleaner and easier
to understand. It is especially useful in OOP or 
console applications, where different cases can trigger
different actions or methods.


# Questions for answers.md:
## 1:
A list comprehension stores all values in memory,
computes them immediately, allows access to any
element and uses square brackets []. A generator expression
produces values one by one, computes them lazily,
must be iterated, and uses parantheses().
If we have small number of elements, need fast access,
and want to get the entire list immediately,
it is better to use list comprehension. On the other
hand, if we have a large number of elements, or we 
do not know the exact number but it is very large,
and we do not need to store all values in memory, 
and we need to compute one value at a time on demand,
then a generator expression is better.


## 2:
Generators are lazy because they compute values only
when there is a request for the computation, and
this allows working with large sequences efficiently.


## 3:
When a generator reaches the end of the function, 
or has executed all its yield statements, any attempt
to get a value through certain functions will raise
StopIteration, which indicates thet there are no more
values and the generator will not return anything else. In other words, 
it does not return values repeatedly, and it can be iterated until
the function ends. When the function ends,
the generator stops and signals that there are no
more values.

