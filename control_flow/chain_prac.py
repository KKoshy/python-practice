"""
This file holds the practice on chain from itertools
"""
from itertools import chain

# chaining multiple iterables
x = [1, 2, 3, 4, 5]
y = [6, 7]
z = [8, 9, 10, 11, 12]
print("Merging multiple iterables")
for value in chain(x, y, z):
    print(value**2)


matrix = [
    [1, 2, 3],
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
]
print("Flattening list of lists")
for value in chain(*matrix):
    print(value*10)
