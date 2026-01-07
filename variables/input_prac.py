"""
This file holds the practice on accepting user input
"""
def performing_addition(func):
    def wrapper(*args, **kwargs):
        print("Invoking actual func")
        result =  func(*args, **kwargs)
        print("After invoking actual func")
        return result
    return wrapper

@performing_addition
def add(*args):
    print("Performing addition")
    return sum(args)


if __name__=="__main__":
    data = input("Enter values in comma separated format: ")
    data = data.split(",")
    data = [int(x.strip()) for x in data if x.strip()]
    value = add(*data)
    print(value)
