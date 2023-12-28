from django.test import TestCase

class YourAppTests(TestCase):
    def test_example(self):
        # Write your test code here
        self.assertEqual(2 + 2, 4)

    def test_another_example(self):
        # Write your test code here
        self.assertTrue(True)

    def test_additional_example(self):
        # Write your test code here
        self.assertEqual("hello".upper(), "HELLO")