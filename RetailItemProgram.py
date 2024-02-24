from RetalItemClass import RetailItem

def main():
    item_one = RetailItem(
        "Jacket",
        12,
        59.95,
    )

    item_two = RetailItem(
        "Designer Jeans",
        40,
        34.95,
    )

    item_three = RetailItem(
        "Shirt",
        20,
        24.95
    )

    print(f"Item #1: {item_one.description}, {item_one.inventory}, {item_one.price}")
    print(f"Item #2: {item_two.description}, {item_two.inventory}, {item_two.price}")
    print(f"Item #3: {item_three.description}, {item_three.inventory}, {item_three.price}")


main()