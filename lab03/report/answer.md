## Answer for 1.Question
Functions are first-class objects in Python 
because they have very powerful features. For example,
a function is a reference to an object: when we 
write _def a()_, the variable a is a variable that 
refers to a function object. 
The second case is thet functions can be
passed as erguments. For example, as in task "A", or
with the _abs_ function we do not call it, but pass
i as a value.
The third case is that we can return functions
(in languages like c++ or c#, there is a way to 
understand if a function returns something: if is 
void, it returns nothing; if it is _int_, _string_,
etc., then it returns some value).
The fourth case is that functions can "remember"
variables this is called _closures_, where a closure
is formed.
The last case is short functions called lambda expressions.


## Answer for 2.Question
The main difference between _lambda_ and _def_ is
that -lambda_ automatically returns a value, 
whereas with _def_ we have to use _return_.
Another difference is that a _lambda_ is a single-line
function, like a quick, short function, while _def_
can contain multiple lines of code describing some
action, _def_ is usually used for larger functions.
Another key difference is that a _def_ function has its
own name, which we use to call it, while a
_lambda_ dies not have a name(unless we assign it to
a variable).
Regarding usage examples: a _def_ function can 
contain loops, docstrings, and more complex logic, 
while a _lambda_ is mainly used for short tasks, 
like sorting or simple transformations.


## Answer for 3.Question
A closure is an inner function. This function has 
access to variables from the outer function. 
When it is used, the variables from the outer function
do not disappear after the closure finishes;
instead, they remain accessible to the inner funstion.
This feature is often used, for example, as a
counter or to store some state.


## Answer for 4.Question
Closures are often used, for example, to store the 
current state when we have multiple functions.
They are also useful when we want to avoid creating
global variables. Additionally, closures are great
for creating parameterized hidden functions.