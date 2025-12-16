from reports.models import EmployeeRecord
from reports.performance import PerformanceReport


def test_performance_report_groups_and_sorts():
    records = [
        EmployeeRecord(
            name="Alex Ivanov",
            position="Backend Developer",
            completed_tasks=45,
            performance=4.8,
            skills="Python, Django, PostgreSQL, Docker",
            team="API Team",
            experience_years=5,
        ),
        EmployeeRecord(
            name="Maria Petrova",
            position="Frontend Developer",
            completed_tasks=38,
            performance=4.2,
            skills="React, TypeScript, Redux, CSS",
            team="Web Team",
            experience_years=4,
        ),
        EmployeeRecord(
            name="John Smith",
            position="Backend Developer",
            completed_tasks=29,
            performance=4.6,
            skills="Python, ML, SQL, Pandas",
            team="AI Team",
            experience_years=3,
        ),
        EmployeeRecord(
            name="Anna Lee",
            position="DevOps Engineer",
            completed_tasks=52,
            performance=4.9,
            skills="AWS, Kubernetes, Terraform, Ansible",
            team="Infrastructure Team",
            experience_years=6,
        ),
    ]

    report = PerformanceReport()
    result = report.generate(records)

    assert result.headers == ["position", "average_performance"]
    assert result.rows == [
        ["DevOps Engineer", 4.9],
        ["Backend Developer", 4.7],
        ["Frontend Developer", 4.2],
    ]
