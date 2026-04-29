import argparse
import logging
from pathlib import Path
import json

from .numbers import parse_numbers, analyze_numbers
from .textstuff import build_sorted_report, build_json_report


def main():
    parser = argparse.ArgumentParser(description="Report Tool")

    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--out", required=True, help="Output file path")
    parser.add_argument("--format", choices=["text", "json"], required=True)
    parser.add_argument("--log-level", default="INFO")

    args = parser.parse_args()

    logging.basicConfig(level=getattr(logging, args.log_level))
    logger = logging.getLogger(__name__)

    logger.info("Reading input file")

    input_path = Path(args.input)
    text = input_path.read_text(encoding="utf-8")

    logger.info("Parsing numbers")
    numbers = parse_numbers(text)

    logger.info("Analyzing numbers")
    stats = analyze_numbers(numbers)

    logger.info("Generating report")

    if args.format == "text":
        output = build_sorted_report(numbers, stats)
    elif args.format == "json":
        output = build_json_report(numbers, stats)

    logger.info("Saving report")

    output_path = Path(args.out)
    output_path.write_text(output, encoding="utf-8")

    logger.info("Done!")


if __name__ == "__main__":
    main()