import argparse
import sys
from pathlib import Path
from typing import Iterable

from tabulate import tabulate

from reports.loader import load_records
from reports.performance import PerformanceReport
from reports.registry import ReportRegistry


def existing_file(path_str: str) -> Path:
    """Argparse type that ensures the file exists."""
    path = Path(path_str)
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"file not found: {path_str}")
    return path


def build_parser(available_reports: Iterable[str]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate reports from CSV files with completed tasks data."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        type=existing_file,
        metavar="PATH",
        help="Path(s) to CSV file(s) with employee data.",
    )
    parser.add_argument(
        "--report",
        required=True,
        choices=sorted(available_reports),
        help="Name of the report to generate.",
    )
    return parser


def build_registry() -> ReportRegistry:
    registry = ReportRegistry()
    registry.register(PerformanceReport())
    return registry


def main(argv: list[str] | None = None) -> int:
    registry = build_registry()
    parser = build_parser(registry.names)
    args = parser.parse_args(argv)

    records = load_records(args.files)
    report = registry.get(args.report)
    result = report.generate(records)

    if not result.rows:
        print("No data available for the requested report.")
        return 0

    print(tabulate(result.rows, headers=result.headers, tablefmt="github", floatfmt=".2f"))
    return 0


if __name__ == "__main__":  # pragma: no cover - convenience entrypoint
    sys.exit(main())
