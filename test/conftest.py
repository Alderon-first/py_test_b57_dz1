from fixture.application import Application
import pytest
import json
import jsonpickle
import os.path
import importlib
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file) # # ищу путь к файлу и поднимаюсь к родительской директории (но путь не универсален для разных ОС) затем os.path.abspath(parent) преобразует путь так, чтобы он склеился правильным образом
        print(config_file)
        with open(config_file) as f:
            target = json.load(f)
            print(target)
    return target


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    print(target)
    web_config = load_config(request.config.getoption("--target"))["web"]
    print(web_config)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DbFixture(host=db_config["host"], name=db_config["name"], user=db_config["user"], password=db_config["password"])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    # перехват значений из командной строки
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    parent = os.path.join(os.path.dirname(__file__),
                          os.pardir)  # ищу путь к файлу и поднимаюсь к родительской директории (но путь не универсален для разных ОС)
    with open( os.path.join(os.path.abspath(parent), "data/%s.json" % file)) as f: # os.path.abspath(parent) преобразует путь так, чтобы он склеился правильным образом
        return jsonpickle.decode(f.read())
