WIDTH = 40


def big_message(s):
    content = [
       "-" * WIDTH,
       "",
       s.center(WIDTH),
       "",
       "-" * WIDTH,
    ]
    return "\n".join(content)


def format_item(left, right):
    left_limit = WIDTH - len(right) - 1
    content = []

    while left:
        current = left[:left_limit]
        left = left[left_limit:]
        if not left:
            content.append(current)
            continue
        if left[0] == " ":
            content.append(current)
            left = left[1:]
            continue
        words = current.split(" ")
        if len(words) == 1:
            content.append(current)
            continue
        before_last_space = " ".join(words[:-1])
        content.append(before_last_space)
        after_last_space = words[-1]
        left = after_last_space + left

    last_line = content[-1].ljust(left_limit) + " " + right

    if len(content) == 1:
        return last_line

    return "\n".join(content[:-1]) + "\n" + last_line


class Market:
    def __init__(self, goods):
        self.goods = goods

    def add_good(self, name, price):
        self.goods[name] = price


class Receipt:
    def __init__(self, market):
        self.market = market
        self.content = {}

    def add_line(self, name, count):
        if name in self.content:
            self.content[name] += count
        else:
            self.content[name] = count

    def render(self):
        total = 0
        content = [
            big_message("Welcome to our shop!"),
            "",
        ]

        for name, count in self.content.items():
            if count > 1:
                left = "{} x {}".format(name, count)
            else:
                left = name
            cost = self.market.goods[name] * count
            total += cost
            right = str(cost)
            content.append(format_item(left, right))

        content.append("")
        content.append("-" * WIDTH)
        content.append("-" * WIDTH)
        content.append("")
        content.append(format_item("Total:", str(total)))
        content.append("")
        content.append(big_message("Thank you!"))

        return "\n".join(content)


if __name__ == "__main__":
    shop = Market({"Beer": 39, "Cigaret": 112})
    shop.add_good("Fish", 19)

    shop_1_receipt = Receipt(shop)

    shop_1_receipt.add_line("Beer", 4)
    shop_1_receipt.add_line("Cigaret", 3)
    shop_1_receipt.add_line("Fish", 2)

    print(shop_1_receipt.render())
