"""
This file holds the practice on try.. except.. else.. finally
"""
import random

value_01 = random.randint(1, 10)
value_02 = random.randint(0, 2)

try:
    print("Initializing divison")
    result = value_01//value_02
except ZeroDivisionError:
    print("Encountered zero division error")
else:
    print(f"Result: {result}")
finally:
    print("Concluding division")
