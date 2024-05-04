# otus-spp-api-prjct
## SPP Panel Automation Tests

Проект по автоматизации API и UI тестов для SPP панели.

## Установка (локально)

Убедитесь, что на вашей машине установлен Python, набрав в консоли:

```
python --version
```
Eсли Python не установлен, перейдите на официальный сайт для установки [Python](https://www.python.org/downloads/).

Установка виртуального окружения - инструмент, который помогает сохранить зависимости, необходимые для разных проектов, путем создания для них изолированных виртуальных окружений python.

Создайте виртуальное окружение. В консоли введите:
```
python -m venv venv
```
Запустите виртуальное окружение
- для Windows:
```
venv\Scripts\activate.bat
```
- для Linux:
```
source venv/bin/activate
```
Установка зависимостей и библиотек:
```
pip install -r requirements.txt
```

## Запуск

Убедитесь, что данные об API-ключе, логине и пароле пользователя - хранятся в переменных окружения на машине, где запускаются тесты.

Запуск API-тестов:
```
pytest ./tests/test_api/ -n 3 --base_endpoint=<api_endpoint> --alluredir=allure-results
```
Запуск UI-тестов:
```
pytest ./tests/test_ui/ -n 3 --executor=local --panel_url=<auth_panel_URL> --browser=<browser_name> --bv=<browser_version> --alluredir=allure-results
```
Для запуска на удаленном сервере Selenoid, укажите его IP адрес: `--executor=<executor_IP>`

Для дальнейшей генерации отчета Allure убедитесь, что Allure установлен на локальную машину, затем воспользуйтесь командой:
```
allure generate allure-results\ --single-file
```
