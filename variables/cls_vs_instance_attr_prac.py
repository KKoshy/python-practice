"""
This file holds the practice on class attributes vs instance attributes
"""
class Product:
    unknown_price = "Ask for details"

    def __init__(self, name, price=None):
        self.name = name
        self.price = price

    def display_price(self):
        if self.price is None:
            return self.unknown_price
        return f"{self.price:.2f}"
	    
duck = Product("rubber duck")
# accessing class attribute via look up
print(duck.unknown_price)
# creating instance attribute
duck.unknown_price = 10
# look up finds the attribute in the instance namespace itself
print(duck.unknown_price)
# class attribute
print(Product.unknown_price)
# deleting the instance attribute
del duck.unknown_price
# again lands on class attribute via look up
print(duck.unknown_price)
