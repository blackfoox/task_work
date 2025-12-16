from __future__ import annotations

from typing import Dict, Iterable, List

from reports.base import Report


class ReportRegistry:
    def __init__(self) -> None:
        self._reports: Dict[str, Report] = {}

    def register(self, report: Report) -> None:
        if report.name in self._reports:
            raise ValueError(f"report already registered: {report.name}")
        self._reports[report.name] = report

    def get(self, name: str) -> Report:
        try:
            return self._reports[name]
        except KeyError as exc:
            raise KeyError(f"report not found: {name}") from exc

    @property
    def names(self) -> List[str]:
        return list(self._reports.keys())

    def __iter__(self) -> Iterable[Report]:
        return iter(self._reports.values())
