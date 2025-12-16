# CSV Report Tool

CLI-скрипт для формирования отчётов по закрытым задачам из CSV-файлов. Сейчас доступен отчёт `performance`, считающий среднюю эффективность по позициям, но архитектура позволяет быстро добавить новые отчёты.

## Установка
- Создать окружение: `python -m venv .venv && .\.venv\Scripts\activate`
- Установить зависимости: `pip install -r requirements.txt`
- Для разработки и тестов: `pip install -r requirements-dev.txt`

## Использование
Пример запуска на готовом файле:
```bash
python report_tool.py --files examples/sample.csv --report performance
```
Вывод:
```
| position          |   average_performance |
|-------------------|-----------------------|
| DevOps Engineer   |                  4.90 |
| Backend Developer |                  4.80 |
| Frontend Developer|                  4.70 |
| Data Scientist    |                  4.60 |
| QA Engineer       |                  4.50 |
```
Можно передать несколько файлов через `--files` — данные будут объединены.

## Тесты
```bash
pytest --cov=reports --cov=report_tool
```

## Как добавить новый отчёт
1. Создать класс, наследующий `reports.base.Report`, реализовать `generate`, вернуть `ReportResult` с `headers` и `rows`.
2. Зарегистрировать отчёт в `build_registry` в `report_tool.py`.
После этого новый отчёт станет доступен через параметр `--report`.
