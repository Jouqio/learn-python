"""Mini Project 09: Inventory Management"""


class InventoryItem:
    def __init__(self, name, quantity, low_stock_threshold=5):
        self.name = name
        self.quantity = quantity
        self.low_stock_threshold = low_stock_threshold

    def is_low_stock(self):
        return self.quantity <= self.low_stock_threshold


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        self.items[name] = InventoryItem(name, quantity)

    def sell(self, name, quantity):
        item = self.items[name]
        if quantity > item.quantity:
            raise ValueError("Not enough stock")
        item.quantity -= quantity

    def low_stock_report(self):
        return [item.name for item in self.items.values() if item.is_low_stock()]


def main():
    inventory = Inventory()
    inventory.add_item("Notebook", 10)
    inventory.sell("Notebook", 7)
    print("Low stock items:", inventory.low_stock_report())


if __name__ == "__main__":
    main()
