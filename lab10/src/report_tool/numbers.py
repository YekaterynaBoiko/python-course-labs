def _cleanup_pieces(parts):
    cleaned = []
    for item in parts:
        item = item.strip()
        if item != "":
            cleaned.append(item)
    return cleaned


def parse_numbers(text: str) -> list[float]:
    text = text.replace(";", ",").replace(" ", ",")

    pieces = text.split(",")
    pieces = _cleanup_pieces(pieces)

    result = []

    for p in pieces:
        result.append(float(p))

    return result


def analyze_numbers(numbers):
    return {
        "min": min(numbers),
        "max": max(numbers),
        "sum": sum(numbers),
        "count": len(numbers),
        "mean": sum(numbers) / len(numbers) if numbers else 0
    }


def sort_numbers(numbers):
    return sorted(numbers)