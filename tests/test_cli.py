import pytest

from report_tool import main


CSV_HEADER = "name,position,completed_tasks,performance,skills,team,experience_years"


def create_csv(path, rows):
    content = "\n".join([CSV_HEADER, *rows])
    path.write_text(content, encoding="utf-8")


def test_cli_outputs_performance_table(tmp_path, capsys):
    first_file = tmp_path / "first.csv"
    second_file = tmp_path / "second.csv"

    create_csv(
        first_file,
        [
            'Alex Ivanov,Backend Developer,10,4.0,"Python",API,2',
            'Maria Petrova,Backend Developer,12,5.0,"Python",API,3',
        ],
    )
    create_csv(
        second_file,
        [
            'John Smith,QA Engineer,8,4.8,"Selenium",QA,4',
            'Anna Lee,Frontend Developer,11,4.6,"React",Web,3',
        ],
    )

    exit_code = main(
        ["--files", str(first_file), str(second_file), "--report", "performance"]
    )
    captured = capsys.readouterr().out

    assert exit_code == 0
    assert "position" in captured
    assert "average_performance" in captured
    assert "QA Engineer" in captured
    assert captured.index("QA Engineer") < captured.index("Backend Developer")


def test_cli_rejects_unknown_report(tmp_path):
    file_path = tmp_path / "data.csv"
    create_csv(
        file_path,
        ['Alex Ivanov,Backend Developer,10,4.0,"Python",API,2'],
    )

    with pytest.raises(SystemExit) as exc_info:
        main(["--files", str(file_path), "--report", "unknown"])

    assert exc_info.value.code == 2
