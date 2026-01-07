"""
This file holds the practice on class, static and instance methods
"""
class Animal:
    kingdom="Animal"

    def __init__(self, color: str, tail: str):
        self.color = color
        self.tail = tail

    @staticmethod
    def find_kingdom():
        print("Animal kingdom")

    @classmethod
    def update_kingdom(cls):
        # class attribute is modified across instances
        cls.kingdom = "Animalia"

    @classmethod
    def limbs(cls):
        print("2 Hind limbs and 2 fore limbs")

    def nature(self):
        print(f"Color: {self.color}")
        print(f"Tail: {self.tail}")

an = Animal('orange', 'small')
bn = Animal('white', 'small')
an.nature()
an.limbs()
an.find_kingdom()
an.update_kingdom()
print(bn.kingdom)
