import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUP")
    yield
    print("Running method level teardown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("Running one time setup")
    if browser == 'firefox':
        value = 30
        print("Running test on FF")
    else:
        value = 45
        print("Running test on Chrome")

    if request.cls is not None:
        request.cls.value = value
    yield value
    print("Running oneTime teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating systems")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("osType")