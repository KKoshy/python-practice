"""
This file holds the practice on duck typing
"""
class Duck:
    def swim(self):
        print("Duck is swimming")

    def fly(self):
        print("Duck is flying")

class Swan:
    def swim(self):
        print("Swan is swimming")

    def fly(self):
        print("Swan is flying")

class Albatross:
    def swim(self):
        print("Albatross is swimming")

    def fly(self):
        print("Albatross is flying")


if __name__ == "__main__":
    duck, swan, albatross = Duck(), Swan(), Albatross()
    birds = [duck, swan, albatross]

    for bird in birds:
        bird.swim()
        bird.fly()
