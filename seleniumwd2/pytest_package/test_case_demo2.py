import pytest

@pytest.yield_fixture()
def setUp():
    print("Running demo2 setUP")
    yield
    print("Running demo2 teardown")

def test_demo2_methodA(setUp):
    print("Running demo2 method A")

def test_demo2_methodB(setUp):
    print("Running demo2 method B")
