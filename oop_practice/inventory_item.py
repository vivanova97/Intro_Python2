"""Problem 7: Inventory Item with Quantity Validation
Create a class InventoryItem that:

Has a private attribute _quantity to store the quantity of an item.
Has a public quantity property with a setter that ensures the quantity is a non-negative integer.
Has a method add_items(amount) to add a certain number of items.
Has a method remove_items(amount) to remove a certain number of items, but ensures the quantity cannot go below 0.
Has a deleter for quantity that resets the quantity to 0."""


class InventoryItem:
    def __init__(self, quantity):
        self.quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if not isinstance(value,int):
            raise TypeError(f"Quantity should be an integer not {type(value)}")
        if value < 0:
            raise ValueError("Quantity cannot be negative.")

        self._quantity = value

    def add_items (self, amount: int):
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Amount to add should be a positive integer.")
        self.quantity += amount

    def remove_items(self, amount: int):
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Amount to add should be a positive integer.")
        self.quantity -= amount

    @quantity.deleter
    def quantity(self):
        self._quantity = 0


if __name__ == "__main__":
    item_1 = InventoryItem(20)
    item_1.add_items(5)
    print(item_1.quantity)
    item_1.remove_items(10)
    print(item_1.quantity)

