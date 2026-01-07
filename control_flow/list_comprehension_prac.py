"""
This file holds the practice on list comprehension
"""

list_comp_01 = [x for x in range(5)]
print(list_comp_01)


list_comp_02 = [x for x in range(10) if x%2==0]
print(list_comp_02)


list_comp_03 = [x*x if x%2==0 else x for x in range(1, 11)]
print(list_comp_03)

# list comprehension with nested for loops
x = 1
y = 2
z = 1
n = 3

permutations = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
print(permutations)
