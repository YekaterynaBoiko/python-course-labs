print("A) Higher-Order Function")

def apply(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result
print(apply(lambda x: x * 2, [1, 2, 3]))

print("\n" + "-"*40 + "\n")


print("B) map")
# Case 1: square all numbers in all list
numbers = [1, 2, 3]
squared = list(map(lambda x: x ** 2, numbers))
print(f"1) Square all numbers in all list: {squared}")

# Case 2: Convert numbers to strings
numbers = [1, 2, 3]
strings = list(map(lambda x: str(x), numbers))
print(f"2) Convert numbers to strings: {strings}")

print("\n" + "-"*40 + "\n")


print("C) filter")
# Case 1: Keep only even numbers
numbers = [5, 10, 15, 20]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Case 2: Numbers greater than 10
numbers = [5, 10, 15, 20]
greater_than_10 =list(filter(lambda x: x > 10, numbers))
print(f"Greater than 10: {greater_than_10}")

print("\n" + "-"*40 + "\n")


print("D) map/filter vs comprehension")
# Case 1: Only even numbers
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squared_evens = list(map(lambda x: x ** 2, even_numbers))
print(f"Result: {squared_evens}")

# Case 2: list comprehension
numbers = [1, 2, 3, 4, 5, 6]
squared_numbers = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Result with comprehensions: {squared_numbers}")

print("\n" + "-"*40 + "\n")


print("E) Simple Decorator")
def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"call #{count}")
        return func(*args, **kwargs)
    return wrapper
@call_counter
def say_hello():
    print("Hello")
say_hello()
say_hello()
say_hello()

print("\n" + "-"*40 + "\n")


print("F) Decorator with Arguments")
def prefix(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{text}: {result}"
        return wrapper
    return decorator
@prefix("INFO")
def get_data():
    return "data"
print(get_data())

print("\n" + "-"*40 + "\n")


print("G) Caching Decorator")
def cache(func):
    saved = {}
    def wrapper(*args):
        if args in saved:
            print(f"Cached result for {args}")
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return wrapper

def binomial(n, k):
    if k == 0 or k == n:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

print("Without caching:", binomial(5, 2))  # result: 10

@cache
def binomial_cached(n, k):
    if k == 0 or k == n:
        return 1
    return binomial_cached(n-1, k-1) + binomial_cached(n-1, k)

print("With caching:", binomial_cached(5, 2))
print("With caching:", binomial_cached(5, 2))