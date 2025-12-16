from pathlib import Path

from reports.loader import load_records


def write_sample_file(path: Path, rows: list[str]) -> None:
    content = "\n".join(rows)
    path.write_text(content, encoding="utf-8")


def test_load_records_reads_multiple_files(tmp_path):
    file_one = tmp_path / "one.csv"
    file_two = tmp_path / "two.csv"

    write_sample_file(
        file_one,
        [
            "name,position,completed_tasks,performance,skills,team,experience_years",
            'Alex,Backend Developer,10,4.5,"Python",Team A,3',
        ],
    )
    write_sample_file(
        file_two,
        [
            "name,position,completed_tasks,performance,skills,team,experience_years",
            'Maria,Frontend Developer,12,4.8,"React",Team B,4',
        ],
    )

    records = load_records([file_one, file_two])

    assert len(records) == 2
    assert records[0].name == "Alex"
    assert records[1].performance == 4.8
