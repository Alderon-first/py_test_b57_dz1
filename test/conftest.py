from fixture.application import Application
import pytest
import json
import os.path
import importlib

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        parent = os.path.join(os.path.dirname(__file__), os.pardir) # ищу путь к файлу и поднимаюсь к родительской директории (но путь не универсален для разных ОС)
        # print(parent)
        config_file = os.path.join(os.path.abspath(parent), request.config.getoption("--target")) # os.path.abspath(parent) преобразует путь так, чтобы он склеился правильным образом
        # print(config_file)
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target["username"], password=target["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


def pytest_addoption(parser):
    # перехват значений из командной строки
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata