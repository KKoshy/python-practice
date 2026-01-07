"""
This file holds the practice on Decorators
"""
def adding_logs(func):
    def wrapper(*args, **kwargs):
        print(f"adding logs for {func.__name__}")
        func(*args, **kwargs)
        print(f"ending logs for {func.__name__}")
    return wrapper

@adding_logs
def greet(name: str):
    print(f"Welcoming {name}")


# asked in Round-01
def mandate_pos(func):
    def wrapper(*args, **kwargs):
        return abs(func(*args, **kwargs))
    return wrapper

@mandate_pos
def diff(num_01: int, num_02: int):
    return num_01 - num_02


greet("May")
print(diff(1, 3))
print(diff(3, 1))
