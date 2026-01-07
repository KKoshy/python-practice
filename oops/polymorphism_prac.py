"""
This file holds the practice on polymorphism
"""
class Jupiter:
    def announce_post(self):
        print("fifth planet")

class Saturn:
    def announce_post(self):
        print("sixth planet")

for planet in [Jupiter(), Saturn()]:
    planet.announce_post()


# Using base class
class Animal:
    def scream(self):
        print("Animal screams")

class Cat(Animal):
    def scream(self):
        print("Cat meows")

class Dog(Animal):
    def scream(self):
        print("Dog barks")

def scream(obj):
    obj.scream()


c = Cat()
scream(c)
d = Dog()
scream(d)

