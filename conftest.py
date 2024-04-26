import json
import pytest
import os

from api_testing.api_methods import GeneralPublicAPIMethods


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption("--base_url")


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
def public_api_client(base_url, api_headers):
    return GeneralPublicAPIMethods(base_url, api_headers)


@pytest.fixture(scope='session')
def auth_token_env():
    return os.environ.get("PUBLIC_API_TOKEN")


def pytest_addoption(parser):
    parser.addoption("--base_url", action="store", default="https://api.serverspace.io/api/v1")
    parser.addoption("--auth_token", action="store",
                     default="042ef82c8751f62ba514d266468e599e2a60b7660f3d1e5080ba98743089e625")


@pytest.fixture()
def read_test_data_from_json(file_path):
    with open(file_path, 'r') as file:
        test_data = json.load(file)
    return test_data
