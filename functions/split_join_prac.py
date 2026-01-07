"""
This file holds the practice on split and join
"""
value = "Hey, hello, how do you do?"
print(f"value: {value}")
print(f"using split: {value.split(",")}")
print(f"using split with maxsplit limit: {value.split(",", maxsplit=1)}")


values = [str(x) for x in range(10)]
print(f"values: {values}")
print(f"using join: {"".join(values)}")
print(f"using join with delimiter: {" ".join(values)}")
