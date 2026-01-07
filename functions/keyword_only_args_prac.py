"""
This file holds the practice on keyword only arguments
"""
# all arguments after *args are always keyword only arguments
def do_something(*args, age, job, state):
    print("Doing something here")
    print(f"Positional args include {args}")
    print(f"age: {age}")
    print(f"job: {job}")
    print(f"state: {state}")


# all arguments right of * are keyword only arguments
def mandate_kwargs(a, b, *, age, job, state):
    print("Working with keyword only arguments")
    print(a, b, age, job, state)


if __name__=="__main__":
    do_something(3, 4, 5, age=12, job="Carpenter", state="TN")
    mandate_kwargs(3, 4, age=45, job="Fisherman", state="KL")
