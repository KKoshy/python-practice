"""
This file holds the practice on method overriding
"""
class Animal:
    def scream(self):
        print("Animal screams")

class Cat(Animal):
    def scream(self):
        print("Cat meows")

class Dog(Animal):
    def scream(self):
        print("Dog barks")


c = Cat()
c.scream()
d = Dog()
d.scream()
