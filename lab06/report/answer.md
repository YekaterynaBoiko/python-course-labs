# Answer to Questions
## 1.
obj.__ dict__ is a dictionary that stores all the attributes of a specific object. 

For example, when we create an object and assign values to its fields (such as a name), these values are automatically stored in dict. When we access the object, we retrieve these values through its attributes. 

It is used for: 
1. accessing object attributes 
2. dynamically modifying attribute values
3. storing the state of an object 

In other words, dict is an internal mechanism in Python used to store and manage the state of an object.

# 2. 
The main difference between a class and an object is that a class is a template that does not contain specific values and is used to create objects. 

An object, on the other hand, is a concrete instance that has its own values and is created from a class. 

A class is abstract, while an object is real.

# 3.
*__ init__* is a constructor in Python that is automatically called when an object is created. It is used to set the initial values of the object. 

It is also used to prepare the object for use. 

The object is already created before init is called.

# 4.
*__ str__* is called by built-in functions such as: print("some object") and str("some object"). 

It is called when Python needs to convert an object into a string for output and for providing a human-readable representation of the object.

# 5.
***is*** in classes checks the identity of an object, meaning whether it is the same object in memory. 

***==*** in classes checks the equality of objects, meaning whether the objects have the same values. The result depends on the __ eq__ method. 

For example, in Task E, there were two identical books that returned True, and another comparison of two different books that returned False, because the books were different.

# 6. 
The *__ eq__* and *__ lt__* methods must work with any object, not only with instances of a specific class. Therefore, the parameter type is defined as a general *object*.

Since Python allows expressions like:
```
book == 4.5
book == "Example text"
```
we need to perform a type check inside the method, such as:
```
if not isinstance(other, Book): 
   return False

```
This also ensures compatibility with *mypy* ***--strict***.
   