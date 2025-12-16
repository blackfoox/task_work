from __future__ import annotations

from collections import defaultdict
from statistics import mean
from typing import Sequence

from reports.base import Report
from reports.models import EmployeeRecord, ReportResult


class PerformanceReport(Report):
    name = "performance"
    description = "Average performance by position."

    def generate(self, records: Sequence[EmployeeRecord]) -> ReportResult:
        performance_by_position: dict[str, list[float]] = defaultdict(list)
        for record in records:
            performance_by_position[record.position].append(record.performance)

        rows = [
            [position, round(mean(values), 2)]
            for position, values in performance_by_position.items()
        ]
        rows.sort(key=lambda row: row[1], reverse=True)

        return ReportResult(headers=["position", "average_performance"], rows=rows)
