import unittest

from app import (
    big_message,
    format_item,
    WIDTH,
    MIN_LEFT_LIMIT,
    Market,
    Receipt,
)


class BigMessageTestCase(unittest.TestCase):
    def test_hyphens(self):
        result = big_message("Some test for our test")
        hyphens_count = result.count("-")
        self.assertEqual(hyphens_count, WIDTH*2)

    def test_lines_count(self):
        result = big_message("Some test for our test")
        line_breaks = result.count("\n")
        self.assertEqual(line_breaks, 4)

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


class ReceiptTestCase(unittest.TestCase):
    def setUp(self):
        self.market = Market(goods={
            "Beer": 39, "Fish": 19
        })

    def test_add_line(self):
        receipt = Receipt(self.market)
        self.assertFalse(receipt.content)
        receipt.add_line(name="Beer", count=3)
        self.assertEqual(receipt.content["Beer"], 3)
        receipt.add_line(name="Fish", count=5)
        self.assertEqual(receipt.content["Beer"], 3)
        self.assertEqual(receipt.content["Fish"], 5)
        receipt.add_line(name="Beer", count=3)
        self.assertEqual(receipt.content["Beer"], 6)
        self.assertEqual(receipt.content["Fish"], 5)

    def test_render_one_good(self):
        receipt = Receipt(self.market)
        receipt.add_line(name="Beer", count=3)
        result = receipt.render()
        result_list = result.split("\n")
        self.assertEqual(len(result_list), 20)
        good_line = result_list[8]
        good_line_list = good_line.split()
        self.assertEqual(len(good_line), WIDTH)
        self.assertEqual(good_line_list, ["Beer", "x", "3", "117"])
        total_line = result_list[13]
        total_line_list = total_line.split()
        self.assertEqual(len(total_line), WIDTH)
        self.assertEqual(total_line_list, ["Total:", "117"])


if __name__ == "__main__":
    unittest.main()
