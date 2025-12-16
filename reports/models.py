from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EmployeeRecord:
    name: str
    position: str
    completed_tasks: int
    performance: float
    skills: str
    team: str
    experience_years: int

    @classmethod
    def from_csv_row(cls, row: dict[str, str]) -> "EmployeeRecord":
        return cls(
            name=row["name"],
            position=row["position"],
            completed_tasks=int(row["completed_tasks"]),
            performance=float(row["performance"]),
            skills=row["skills"],
            team=row["team"],
            experience_years=int(row["experience_years"]),
        )


@dataclass
class ReportResult:
    headers: list[str]
    rows: list[list[object]]
