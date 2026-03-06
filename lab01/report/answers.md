## Task A - Binding vs Rebinding
Value b still refers to the old value 5,
because in Python we only store references to objects.
At first, a and b both point to the same object 5.
Then we rebind value a to a different object 7.
Meanwhile, value b remains linked to the old object 5,
because we did not change it.

## Task B - Mutation vs Rebinding
- a and b are both bound to the same list.
When we do b.append(3), we mutate the object itself,
so value a also sees the new element.
- The difference between mutation and rebinding:
__Mutation__ changes the object that the names refer to.
__Rebinding__ only changes the name to object binding;
the object itself does not change.

## Task C - Function arguments are new bindings
We  created a list a, which is initiallz emptz.
Using the mutation function, we add 1 to it;
the object changes, and the list becomes a  = [1]
In the rebind function, we assign lst = [2,3],
but when we call the function with the variable a, 
it does not change because we are not modifying 
the object a refers to.

## Task D - Default argument trap 
The list created only once when Python reads the
function definition x = []. Each subsequent
call to the function reuses the same list, simply
adding new elements to it.

## Task E - Copy semantics (shallow vs deep)
- Since a shallow copy creates a new container but
keeps the inner objects the same, when we do a = b
and then add 3 to b, the list a also changes.
- A deep copy creates completely new objects, so the
- variable c just copies the initial state of a and 
- does not change when b is mutated.

## Task F - Reference counting / GC (Python)
For 5 the result looks weird because CPython optimizes
small numbers, they are immortal, always in
memory, just an impplementation detail, 
not guaranteed by Python.