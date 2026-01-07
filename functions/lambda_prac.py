"""
This file holds the practice on lambda expressions
"""
import random

values = [random.randint(1, 100) for _ in range(5)]

squared = lambda values: [x**2 for x in values]

seventh = lambda x, y: x+y

print(f"For {values}, squared results: {squared(values)}")
print(f"For {values[3]}, {values[4]}, add result: {seventh(values[3], values[4])}")
