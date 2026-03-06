import copy
import sys

print("A) Binding / Rebinding")
a = 5
b = a
print(f"a = {a}, b = {b}")
print(f"id(a) = {id(a)}, b = {id(b)}")
a = 7
print("After rebinding a = 7: ")
print(f"a = {a}, b = {b}")
print(f"id(a) = {id(a)}, b = {id(b)}")

print("\n" + "-"*40 + "\n")


print("B) Mutation vs Rebinding")
a = [1, 2]
b = a
print(f"a and b before mutation: \na = {a} \nb = {b}")
print(f"id a = {id(a)} \nid b = {id(b)}")
b.append(3)
print(f"a and b after mutation: \na = {a} \nb = {b}")
print(f"id(a) == id(b): id(a) = {id(a) == id(b)}")

print("\n" + "-"*40 + "\n")


print("C) Function arguments are new bindings")
a = []
print(f"Before call: a = {a}")
# Case 1 mutation
def mutate_list(lst):
    lst.append(1) # changes object
mutate_list(a)
print(f"After mutate_list(a): a = {a}")
# Case 2 - rebinding
def rebind_list(lst):
    lst = [2, 3]
rebind_list(a)
print(f"After rebind_list(a): a = {a}")

print("\n" + "-"*40 + "\n")


print("D) Default argument trap")
def f(x=[]):
    x.append(1)
    return x
print(f"First call: {f()}")
print(f"Second call: {f()}")

print("\n" + "-"*40 + "\n")


print("E) Copy semantics (shallow vs deep")
a = [[1, 2]]
b = a.copy() # shallow copy
c = copy.deepcopy(a) # deep copy
print(f"Original: a = {a}")
b[0].append(3)
print(f"After nodifying b: \na = {a} \nb = {b} \nc = {c}")

print("\n" + "-"*40 + "\n")


print("F) Reference counting / GC (Python)")
# Part 1
x = []
print(f"Refcount(x) = {sys.getrefcount(x)}")
y = x
print(f"Refcount after y = x: {sys.getrefcount(x)}")
# Part 2
a = 5
b = 123456
print(f"Refcount after a = 5: {sys.getrefcount(a)}")
print(f"Refcount after b = 123456: {sys.getrefcount(b)}")
