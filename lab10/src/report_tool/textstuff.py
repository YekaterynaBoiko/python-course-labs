import json
from .numbers import sort_numbers

def build_json_report(numbers, stats):
    return json.dumps({
        "numbers": numbers,
        "stats": stats,
    }, indent=2)

def line_maker(name: str, value) -> str:
    return f"{name}: {value}"


def pretty_title(text: str) -> str:
    return text.strip().title()


def build_sorted_report(numbers: list[float], stats: dict) -> str:
    ordered = sort_numbers(numbers)

    lines = [
        pretty_title("number report"),
        "-" * 20,
        line_maker("count", stats["count"]),
        line_maker("sum", stats["sum"]),
        line_maker("min", stats["min"]),
        line_maker("max", stats["max"]),
        line_maker("mean", round(stats["mean"], 2)),
        line_maker("sorted", ordered),
    ]

    return "\n".join(lines)


def internal_banner():
    return "=" * 30

