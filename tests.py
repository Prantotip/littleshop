import unittest

from app import (
    big_message,
    WIDTH,
)


class BigMessageTestCase(unittest.TestCase):
    def test_hyphens(self):
        result = big_message("Some test for our test")
        hyphens_count = result.count("-")
        self.assertEqual(hyphens_count, WIDTH*2)

    def test_lines_count(self):
        result = big_message("Some test for our test")
        lines_count = result.count("\n")
        self.assertEqual(lines_count, 4)

    def test_content(self):
        test_string = "Some test for our test"
        test_string_centered = test_string.center(WIDTH)
        result = big_message(test_string)
        self.assertEqual(result.split("\n")[2], test_string_centered)
        

if __name__ == '__main__':
    unittest.main()
