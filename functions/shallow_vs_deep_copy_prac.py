"""
This file holds the practice on shallow and deep copy
"""
import copy
import random


print("Shallow copy example")
values = [random.randint(1, 50) for _ in range(10)]
values[-1] = [0, 1]
print(f"Values considered: {values}")
sh_copy = copy.copy(values)
sh_copy[-1][1] = "updated_value"
print(f"Shallow copied values updated: {sh_copy}")
print(f"Actual values again: {values}")


print("Deep copy example")
values = [random.randint(1, 50) for _ in range(10)]
values[-1] = [0, 1]
print(f"Values considered: {values}")
dp_copy = copy.deepcopy(values)
dp_copy[-1][1] = "updated_value"
print(f"Deep copied values: {dp_copy}")
print(f"Actual values now: {values}")
