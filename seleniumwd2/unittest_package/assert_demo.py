"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
"""
import unittest

class AssertDemo(unittest.TestCase):

    def test_AssertTruFalse(self):
        a = True
        self.assertTrue(a, "a is not false")
        b = False
        self.assertFalse(b, "b is not true")

    def test_AssertEqual(self):
        a = "True"
        b = "True"
        self.assertEqual(a,b, msg="'a' is not equal to 'b'")


if __name__ == '__main__':
    unittest.main(verbosity=2)