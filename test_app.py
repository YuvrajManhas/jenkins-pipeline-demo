import unittest
from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertIn("Hello", greet("World"))


if __name__ == "__main__":
    unittest.main()
