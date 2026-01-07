"""
This file holds the practice on zip method
"""
# parallel iteration with zip
for x, y in zip(range(5), range(10)):
    print(x, y)

# zip is lazy - forms iterator from iterables
numbers = zip(range(10), range(5))
print(numbers)
print(next(numbers))
print(next(numbers))
print(list(numbers))

# create dict from 2 iterables using zip
num_log = dict(zip(range(5), range(10)))
print(num_log)

# using strict with zip, comes in > python 3.10
numbers = zip(range(10), range(20), strict=True)
print(numbers)
print(list(numbers))
