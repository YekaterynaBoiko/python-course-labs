# Answer for Questions
## 1.
Duck typing is a concept in Python where what matters is what an object is able to do. In one word: whether this object has the required method or something similar.
An example is:
```
def export(obj):
    print(obj.serialize())
```
The main advantages of duck typing are that it is flexible, has fewer dependencies between classes, and makes the code easier to extend.

## 2.
Protocol works through structural typing, does not require inheritance, and an object is considered valid if it has the required methods. It is also a very flexible approach. An example is Task A. 

Meanwhile, ABC requires explicit inheritance and forces the implementation of abstract methods. It is a more strict and controlled approach and uses nominal typing. 

For example, Task D: the class must explicitly inherit from *SerializableABC*, otherwise it is not considered valid.

## 3.
Protocol does not require inheritance because it is based on duck typing rather than inheritance. 
This means: 
- An object is considered valid if it has the required methods 
- There is no need to explicitly inherit from a Protocol
-  The type system checks the behavior of the object, not its class hierarchy.

## 4.
ABC solves the problem of the lack of strict control over interface implementation in OOP. 
ABC: 
- Forces subclasses to implement all abstract methods 
- Does not allow creating incomplete classes 
- Raises an error at the class definition stage 
- Defines a clear class hierarchy structure

Because without ABC:
- A class may forget to implement the required methods 
- Errors appear only at runtime 
- There is no guarantee that classes follow the same “contract”

## 5.
`@dataclass` is a decorator that automatically generates standard boilerplate code for a class, similar to Copilot. When a class is created, it automatically adds methods like the constructor `__init__`, the `__repr__` method, and other utility methods.

## 6.
When using slots, the way object attributes are stored changes. 
Specifically: 
- Dynamic addition of new attributes is not allowed 
- `__dict__` is not created 
- Less memory is used 
- Sometimes, but not always, attribute access is faster

## 7.
It works with different types of classes because it uses duck typing instead of inheritance-based type checking. 

It does not care which class the object inherits from or how the data is stored inside the object. It only matters whether the object has the required methods with the correct signature, and that is all. 
A more detailed explanation of *Protocol* is provided in **question 1**.