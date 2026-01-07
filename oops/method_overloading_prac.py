"""
This file holds the practice on method overloading
"""
def default_args_overloading(a, b=1, c=2):
    print("Using default arguments")
    return sum([a, b, c])


print(f"sum: {default_args_overloading(a=2)}")
print(f"sum: {default_args_overloading(a=2, b=3)}")
print(f"sum: {default_args_overloading(a=2, b=3, c=4)}")


def variable_pos_overloading(*args):
    print("Using variable positional arguments")
    return sum(args)

print(f"sum: {variable_pos_overloading(2)}")
print(f"sum: {variable_pos_overloading(2, 3)}")
print(f"sum: {variable_pos_overloading(2, 3, 4)}")
