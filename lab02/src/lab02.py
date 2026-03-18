print("A) Truthiness")
values = [0, 1, [], [1], "", "hello", None]
for i in values:
    print(f"value: {i} -> {bool(i)}")

print("\n" + "-"*40 + "\n")


print("B) Identity vs Equality")
a = [1, 2, 3]
b = [1, 2, 3]

#case 1: equal values but different objects
print("Case1: ")
print("a == b -> ", a == b)
print("a is b -> ", a is b)
print()

# case 2 identical objects
c = a
print("Case2: ")
print("a == c ->", a == c)
print("a is c -> ", a is c)
print()

# case 3 behavior with immutable values
x_example = 200
y_example = 200
print("Case 3: ")
print("x_example == y_example -> ", x_example == y_example)
print("x_example is y_example -> ", x_example is y_example)

print("\n" + "-"*40 + "\n")


print("C) Control Flow")
print()
print("Case1: ")
def describe_number(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    elif x < 10:
        return "Small positive"
    else:
        return "large positive"
print(describe_number(-10))
print(describe_number(0))
print(describe_number(1))
print(describe_number(20))
print()
print("Case 2: ")
# elif for all
def describe_number1(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    elif x < 10:
        return "Small positive"
    elif x >= 10:
        return "Large positive"
print(describe_number1(-10))
print(describe_number1(0))
print(describe_number1(1))
print(describe_number1(20))

print("\n" + "-"*40 + "\n")


print("D) Pattern Matching")
def events_processing(event):
    match event:
        case ("click", x, y):
            print(f"click at {x} {y}")
        case ("keypress", key):
            print(f"key pressed: {key}")
        case ("quit",):
            print("quit event")
        case _:
            print("unkown event")

# examples:
events = [
    ("click", 10, 50),
    ("keypress", "A"),
    ("quit",)
]
for event in events:
    events_processing(event)

print("\n" + "-"*40 + "\n")


print("E) Comprehensions")
# case 1:
list_squares = [x**2 for x in range(1, 21)]
print(list_squares)
# case 2:
list_evenSquares = [x for x in range(1, 21) if x % 2 == 0]
print(list_evenSquares)
# case 3:
dictionary_squares = {x: x**2 for x in range(1, 21)}
print(dictionary_squares)

print("\n" + "-"*40 + "\n")


print("F) Generators")
def even_numbers(limit):
    for x in range(0, limit, 2):
        yield x # return one value at a time
for number in even_numbers(10):
    print(number)

# additional requirement:
result = sum(x**2 for x in even_numbers(1000000) if x**2 < 1000000)
print("Sum of even numbers: {}".format(result))