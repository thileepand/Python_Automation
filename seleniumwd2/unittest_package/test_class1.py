import unittest
import unittest_package.test_case_demo2

class TestClass1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#"*30)
        print("Class 1-> class level setup")
        print("#" * 30)

    def setUp(self):
        print("#"*30)
        print("Class 1 -> setup")
        print("#" * 30)

    def test_class1_methodA(self):
        print("#"*30)
        print("Running class 1 -> method A")
        print("#" * 30)

    def test_class1_methodB(self):
        print("#" * 30)
        print("Running class 1 -> method B")
        print("#"*30)

    def tearDown(self):
        print("Class 1 -> teardown")

    @classmethod
    def tearDownClass(cls):
        print("#"*30)
        print("Class 1 -> level tear down class")

if __name__ == "__main__":
    unittest.main(verbosity=2)