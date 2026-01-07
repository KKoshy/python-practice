"""
This file holds the practice on multi level inheritance
"""
class A:
    def show(self):
        print("Inside class A")

class B(A):
    def show(self):
        print("Inside class B")
        super().show()

class C(B):
    def show(self):
        print("Inside class C")
        super().show()

class D(C):
    def show(self):
        print("Inside class D")
        super().show()


d = D()
d.show()
