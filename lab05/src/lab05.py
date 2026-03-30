from typing import List, Optional, Callable, TypeVar, Iterator
print("A) Basic Type Hints")
def add(a: int, b: int) -> int:
    return a + b

def square_list(data: List[int]) -> List[int]:
    return [x * x for x in data]

# Example using:
if __name__ == "__main__":
    return_add: int = add(1, 2)
    print(f"add(1, 2) = {return_add}")

    numbers: List[int] = [1, 2, 3, 4, 5]
    result_square_list: List[int] = square_list(numbers)
    print(f"result_square_list = {result_square_list}")

print("\n" + "-"*40 + "\n")


print("B) Typed Collections")
def filter_even(data: List[int]) -> List[int]:
    return [x for x in data if x % 2 == 0]

if __name__ == "__main__":
    numbers2: List[int] = [1, 2, 3, 4, 5]
    even_numbers2: List[int] = filter_even(numbers2)

    print(f"Original list = {numbers2}")
    print(f"Filtered list = {even_numbers2}")

print("\n" + "-"*40 + "\n")


print("C) Optional")
def find(data: List[int], x: int) -> Optional[int]:
    for item in data:
        if item == x:
            return item
    return None
if __name__ == "__main__":
    numbers3: List[int] = [1, 2, 3, 4, 5]
    found_numbers3: Optional[int] = find(numbers3, 3)
    print(f"Find 3: {found_numbers3}") # result: 3

    # not found:
    not_found: Optional[int] = find(numbers3, -1)
    print(f"Find -1: {not_found}") # result: none

print("\n" + "-"*40 + "\n")


print("D) Function Type")
def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

if __name__ == "__main__":
    def square(n: int) -> int:
        return n * n

    def increment(n: int) -> int:
        return n + 1

    result1: int = apply(square, 3) # 9 => 3 * 3
    print(f"apply(square, 3) = {result1}")

    result2: int = apply(increment, 3) # 4 => 3 + 1
    print(f"apply(increment, 3) = {result2}")

print("\n" + "-"*40 + "\n")


print("E) Generics")
T = TypeVar("T")

def first(items: List[T]) -> T:
    return items[0]

if __name__ == "__main__":
    numbers_part4: List[int] = [1, 2, 3, 4, 5]
    first_number: int = first(numbers_part4) # 1
    print(f"First number: {first_number}")

    words: List[str] = ["Hello", "banana", "Vasya"]
    first_word: str = first(words) # Hello
    print(f"First word: {first_word}")

print("\n" + "-"*40 + "\n")


print("F) Function Returning Function")

def make_multiplier(k: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * k
    return multiplier

if __name__ == "__main__":
    times2: Callable[[int], int] = make_multiplier(2)
    times3: Callable[[int], int] = make_multiplier(3)

    res1: int = times2(5)
    print(f"times2 = {res1}") # 10

    res2: int = times3(5)
    print(f"times3 = {res2}") # 15

print("\n" + "-"*40 + "\n")


print("G) Pipeline")

input_numbers: List[int] = [1, 2, 3, 4, 5]

even_numbers3: Iterator[int] = (x for x in input_numbers if x % 2 == 0)
squared = (x * x for x in even_numbers3)

final_result: int = sum(squared)

print(f"Final result: {final_result}") # 20