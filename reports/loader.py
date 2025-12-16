from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, List

from reports.models import EmployeeRecord

CSV_ENCODING = "utf-8"


def load_records(files: Iterable[Path]) -> List[EmployeeRecord]:
    records: List[EmployeeRecord] = []
    for path in files:
        with path.open(newline="", encoding=CSV_ENCODING) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                records.append(EmployeeRecord.from_csv_row(row))
    return records
