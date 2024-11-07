"""Problem 6: Shopping Cart System
Objective: Create a class called ShoppingCart with the following features:

Implement __init__ to initialize the cart.
Implement __add__ to add an item to the cart.
Implement __sub__ to remove an item from the cart.
Implement __len__ to return the number of items in the cart.
Implement __getattribute__ to restrict access to private methods that shouldn't be accessed directly.
Implement a method calculate_total() to return the total cost of the items in the cart."""

class ShoppingCart:
    def __init__(self, shopping_cart: dict=None):
        if shopping_cart is None:
            self.shopping_cart = dict()


    def __add__(self, item_info: tuple):
        item, quantity, price = item_info

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")

        if item in self.shopping_cart:
            self.shopping_cart[item]['quantity'] += quantity
        else:
            self.shopping_cart[item] = {'quantity': quantity, 'price': price}
        return self


    def __sub__(self, item_quantity: tuple):
        item, quantity = item_quantity
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        if item in self.shopping_cart:
            self.shopping_cart[item]['quantity'] -= quantity
            if self.shopping_cart[item]['quantity'] <= 0:
                self.shopping_cart.pop(item)
        return self


    def __len__(self):
        return sum(value['quantity'] for value in self.shopping_cart.values())


    def calculate_total(self):
        return sum(value['price'] * value['quantity'] for value in self.shopping_cart.values())


    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError(f"Access to private method '{name}' is restricted!")
        object.__getattribute__(self, name)


if __name__ == '__main__':
    shopping_cart_1 = ShoppingCart()
    shopping_cart_1 + ('banana', 5, 0.50)
    shopping_cart_1 + ('sugar', 1, 2.50)
    shopping_cart_1 + ('rice', 2, 1.50)
    shopping_cart_1 - ('rice', 1)
    shopping_cart_1 - ('sugar', 1)
    print(shopping_cart_1.__len__())
    print(shopping_cart_1.shopping_cart)
    print(shopping_cart_1.calculate_total())
