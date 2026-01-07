"""
This file holds the practice on isinstance 
"""
class A:
    def __init__(self, name):
        self.name = name

    def find(self):
        print("Found an object with match")


class B(A):
    def __init__(self, name, track):
        super().__init__(name)
        self.track = track

    def play(self):
        print(f"Playing {self.track} of {self.name}")



if __name__== "__main__":
    b = B("Bruno", "Die with a smile")
    b.play()
    print("Checking if b is an instance of B")
    print(isinstance(b, B))
    print("Checking if b is an instance of A")
    print(isinstance(b, A))
