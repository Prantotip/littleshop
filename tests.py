import unittest

from app import (
    big_message,
    format_item,
    WIDTH,
    MIN_LEFT_LIMIT,
    Market,
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


class FormatItemTestCase(unittest.TestCase):
    def test_short_left(self):
        left = "Some test"
        right = "I need some sleep"
        spaces_count = WIDTH - len(left) - len(right)
        result = format_item(left, right)
        self.assertEqual(result, left + " "*spaces_count + right)

    def test_middle_left(self):
        left = "Some test for our test"
        right = "I need some sleep"
        spaces_count = WIDTH - len(left) - len(right)
        result = format_item(left, right)
        self.assertEqual(result, left + " "*spaces_count + right)

    def test_long_left(self):
        left = (
            "Some test for our test I need some sleep "
            "Some test for our test I need some sleep"
        )
        right = "I need some sleep"
        spaces_count = WIDTH - len(left) - len(right)
        result = format_item(left, right)

        if WIDTH < 99:
            self.assertIn("\n", result)
        else:
            self.assertNotIn("\n", result)

        self.assertTrue(result.endswith(right))

    def test_exception(self):
        left = "Some test for our test, I need some sleep"
        right = "I"*WIDTH
        spaces_count = WIDTH - len(left) - len(right)
        with self.assertRaises(ValueError) as cm:
            format_item(left, right)
        self.assertEqual(
            str(cm.exception),
            "Right must be {} characters or less".format(
                WIDTH - MIN_LEFT_LIMIT - 1
            )
        )


class MarketTestCase(unittest.TestCase):
    def test_add_good(self):
        market = Market(goods={})
        self.assertFalse(market.goods)
        market.add_good(name="Beer", price=39)
        self.assertEqual(market.goods["Beer"], 39)


if __name__ == '__main__':
    unittest.main()
