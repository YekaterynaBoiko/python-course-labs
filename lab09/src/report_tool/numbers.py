def _cleanup_pieces(parts):
    cleaned = []
    for item in parts:
        item = item.strip()
        if item != "":
            cleaned.append(item)
    return cleaned


def parse_numbers(text: str) -> list[float]:
    pieces = text.replace(";", ",").split(",")
    pieces = _cleanup_pieces(pieces)
    result = []

    for p in pieces:
        result.append(float(p))

    return result


def _check_input(numbers):
    if not numbers:
        raise ValueError("numbers must not be empty")


def analyze_numbers(numbers: list[float]) -> dict:
    _check_input(numbers)

    total = sum(numbers)
    count = len(numbers)
    avg = total / count

    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": avg,
    }


def sort_numbers(numbers: list[float]) -> list[float]:
    return sorted(numbers)


def _demo_data():
    return [1, 2, 3, 4, 5]


if __name__ == "__main__":
    print("Module: numbers")
    print("Provides utilities for parsing and analyzing numeric data. \n")

    print("Public functions:")
    print("- parse_numbers(text)")
    print("- analyze_numbers(numbers)")
    print("- sort_numbers(numbers)")

    example_data = "1, 2; 3, 4"
    nums = parse_numbers(example_data)

    print(f"Example input: {example_data}")
    print(f"Parsed: {nums}")
    print(f"Analysis: {analyze_numbers(nums)}")
    print(f"Sorted: {sort_numbers(nums)}")
