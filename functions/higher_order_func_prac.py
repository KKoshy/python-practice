"""
This file holds the practice on higher order functions
"""
import random
import os

rand_values = [random.randint(1, 100) for _ in range(10)]
print(f"Values considered: {rand_values}")


print("Map example")
def seventh_table(x):
    return x*7
new_value = map(seventh_table, rand_values)
print(list(new_value))


new_value = map(lambda x: x*7, rand_values)
print(list(new_value))

print("Filter example")
def is_prime(num):
    if num<2:
        return False
    elif num==2:
        return True
    else:
        for x in range(2, num):
            if num%x==0:
                return False
        return True
    
prime_values = filter(is_prime, rand_values)
print(list(prime_values))

even_values = filter(lambda x:x%2==0, rand_values)
print(list(even_values))


print("Sorted example")
files_ex = ['file01.html', 'file03.html', 'file01.png', 'file02.jpeg', 'file02.html', "data.csv", "report.txt", "image.png", "notes.md", "archive.zip"]

files_op = sorted(files_ex, key=lambda f: os.path.splitext(f)[1])
print(f"files considered: {files_ex}")
print(f"files sorted: {files_op}")
