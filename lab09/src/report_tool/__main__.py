from .numbers import parse_numbers, analyze_numbers
from .textstuff import build_sorted_report
from .saveit import save_report, read_back


def show_help():
    print("Report tool")
    print("This tool processes numeric data and generates reports.\n")

    print("Main capabilities:")
    print("- Parse numbers from text")
    print("- Analyze numeric data")
    print("Generate formatted reports")
    print("- Save reports to file\n")

    print("Example input:")
    print('  "1, 2, 3, 4.5"\n')


def example_workflow():
    text = "4, 8, 15, 16, 23, 42"
    numbers = parse_numbers(text)
    stats = analyze_numbers(numbers)
    report = build_sorted_report(numbers, stats)
    return report


def main():
    show_help()
    report = example_workflow()
    print(report)

    path = save_report(report, "report_output")

    print("\nSaved to:", path)
    print("\nSaved file content:")
    print(read_back(str(path)))




if __name__ == "__main__":
    main()