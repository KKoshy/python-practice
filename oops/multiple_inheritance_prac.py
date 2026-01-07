"""
This file holds the practice on multiple inheritance
"""
class A:
    def summarize(self):
        print("Animal A")

    def carbon(self):
        print("Carbon A")

class ASub:
    def summarize(self):
        print("Animal ASub")

    def carbon(self):
        print("Carbon ASub")


class B(A, ASub):
    def summarize(self):
        print("Animal B")
        super().summarize()

    def carbon(self):
        print("Carbon B")
        super().carbon()

class C(A):
    def summarize(self):
        print("Animal C")
        # super().summarize()

class D(C, B):
    def summarize(self):
        print("Animal D")
        super().summarize()
        super().carbon()


dobj = D()
dobj.summarize()
print(D.mro())
