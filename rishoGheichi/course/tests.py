from django.test import TestCase


# class CourseCommnetTest(TestCase):
#     pass


class Calculator:
    def sum(self, a, b):
        return a+b+1

    def multiply(self, a, b):
        return a*b


class CalculatorTest(TestCase):

    def setUp(self):
        print("in setup")

    @classmethod
    def setUpClass(cls):
        cls.cal = Calculator()
        print("in class setUp")

    def test_sum(self):
        a, b = 5, 8
        c = self.cal.sum(a, b)
        self.assertEqual(c, 13)

    def test_multiply(self):
        a, b = 5, 8
        c = self.cal.multiply(a, b)
        self.assertEqual(c, 40)

    def tearDown(self):
        print("in tearDoen")

    @classmethod
    def tearDownClass(cls):
        print("in class tearDown")
