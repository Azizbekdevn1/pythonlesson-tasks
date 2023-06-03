import unittest
from twoClass import MyClass1, MyClass2


class TestMyClass1(unittest.TestCase):
    def setUp(self):
        self.obj1 = MyClass1("John")

    def test_say_hello(self):
        expected_output = "Hello from MyClass1! My name is John"
        self.assertEqual(self.obj1.say_hello(), expected_output)


class TestMyClass2(unittest.TestCase):
    def setUp(self):
        self.obj2 = MyClass2(42)

    def test_print_value(self):
        expected_output = "The value is 42"
        self.assertEqual(self.obj2.print_value(), expected_output)


unittest.main()
