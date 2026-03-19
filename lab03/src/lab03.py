print("A) Functions as Objects")
def apply_twice(func, x):
    return func(func(x))
#Example 1:
result = apply_twice(lambda x: x + 1, 3)
print(result)

#Example 2:
result2 = apply_twice(abs, 2)
print(result2)

#Example 3:
def square(x):
    return x * x
result3 = apply_twice(square, 3)
print(result3)

print("\n" + "-"*40 + "\n")


print("B) Sorting with Lambda")
people = [
    ("Alice", 25),
    ("Bob", 20),
    ("Carol", 30),
    ("Dave", 22)
]

#Case 1: sorted by age:
sorted_by_age = sorted(people, key=lambda x: x[1])
print(f"Sorted by age: {sorted_by_age}")
#Case 2: sorted by name:
sorted_by_name = sorted(people, key=lambda x: x[0])
print(f"Sorted by name: {sorted_by_name}")

print("\n" + "-"*40 + "\n")


print("C) Function Factory")
def make_multiplier(k):
    def multiplier(n):
        return n * k
    return multiplier

times3 = make_multiplier(3)
times10 = make_multiplier(10)
print(times3(10))
print(times10(10))

print("\n" + "-"*40 + "\n")


print("D) Closure Counter")
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())
print(c())

# another one more example
d = counter()
print(d())
print(d())

print("\n" + "-"*40 + "\n")


print("E) Lambda vs def")
# using def:
def square_def(x):
    return x * x
print("using def: ")
print(square_def(5))
print(square_def(25))

#using lambda
square_lambda = lambda x: x * x
print("using lambda: ")
print(square_lambda(5))
print(square_lambda(25))

print("\n" + "-"*40 + "\n")


print("F) Functional Composition")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = filter(lambda x: x % 2 == 0, numbers) # only even making
result = sum(x**2 for x in evens)
print(result)

print("\n" + "-"*40 + "\n")
