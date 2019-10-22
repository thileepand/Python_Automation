"""
file name should start with test
test method name should start with test

py.test test_mod.py    #run test in module
py.test somepath       #run all test below somepath
py.test test.module.py::test_method #Only run test_method in test_module

-s to print statement
-v verbose
"""

import pytest

@pytest.yield_fixture()
def setUp():
    print("Running demo3 setup")
    yield
    print("Running demo3 teardown")

def test_demo3_methodA(setUp):
    print("Running demo3 method A")

def test_demo3_methodB(setUp):
    print("Running demo3 method B")
