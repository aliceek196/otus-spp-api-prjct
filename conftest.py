import json
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api_testing.api_methods import GeneralPublicAPIMethods


@pytest.fixture(scope='session')
def base_endpoint(request):
    return request.config.getoption("--base_endpoint")


@pytest.fixture(scope='session')
def auth_token(request):
    return request.config.getoption("--auth_token")


@pytest.fixture(scope='session')
def api_headers(auth_token):
    headers = {
        'x-api-key': auth_token
    }
    return headers


@pytest.fixture(scope='session')
def public_api_client(base_endpoint, api_headers):
    return GeneralPublicAPIMethods(base_endpoint, api_headers)


def pytest_addoption(parser, api_key=None):
    parser.addoption("--base_endpoint", action="store", default="https://api.serverspace.io/api/v1")
    parser.addoption("--auth_token", action="store",
                     default=api_key)
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--panel_url", action="store", default="https://auth.ss4test.com")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--executor", action="store", default="93.183.73.3", help="Use 'local' to run tests locally")
    parser.addoption("--bv", action="store", default="123.0")


@pytest.fixture(scope="session")
def auth_token():
    # Получаем ключ API из переменной окружения
    api_key = os.environ.get("AUTH_TOKEN")
    if not api_key:
        raise ValueError("API key not found in environment variable AUTH_TOKEN")
    return api_key


@pytest.fixture()
def read_test_data_from_json(file_path):
    with open(file_path, 'r') as file:
        test_data = json.load(file)
    return test_data


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    panel_url = request.config.getoption("--panel_url")
    headless = request.config.getoption("--headless")

    if executor == "local":
        driver = create_local_driver(browser_name, headless)
    else:
        driver = create_remote_driver(browser_name, version, executor)

    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get(panel_url)

    driver.panel_url = panel_url

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver


def create_local_driver(browser_name, headless):
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    return driver


def create_remote_driver(browser_name, version, executor):
    executor_url = f"http://{executor}:4444/wd/hub"

    if browser_name == "chrome":
        options = ChromeOptions()
    elif browser_name == "firefox":
        options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    options.browser_version = version

    driver = webdriver.Remote(
        command_executor=executor_url,
        options=options
    )
    return driver
