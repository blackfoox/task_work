from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

from reports.models import EmployeeRecord, ReportResult


class Report(ABC):
    """Base class for all reports."""

    name: str
    description: str

    @abstractmethod
    def generate(self, records: Sequence[EmployeeRecord]) -> ReportResult:
        """Build the report for the given records."""
