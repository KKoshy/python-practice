"""
This file holds the practice on namespaces
"""
# Built-in namespace
print("Hello there, this is from a built-in namespace")

# Global namespace
global_warm = 10
capsicum = "green"
print(f"Global value for global_warm: {global_warm}")
print(f"Accessing all the global namespaces: {globals()}")


def add_logs(func):
    # Enclosing namespace
    global_warm = 15
    fisher = "fishing 15"
    print(f"Enclosing value for global_warm: {global_warm}")
    def wrapper(*args, **kwargs):
        # Local namespace
        global_warm = 5
        print(f"Local value for global_warm: {global_warm}")
        print("Starting the target method...")
        func(*args, **kwargs)
        print("Target method terminated")
        print("Accessing enclosing value of fisher from local")
        nonlocal fisher
        print(f"Enclosing value of fisher from local: {fisher}")
        global capsicum
        print(f"Accessing global value of capsicum from local: {capsicum}")
        print(f"Accessing all local values: {locals()}")
    return wrapper


@add_logs
def greet(name: str):
    print(f"Hey {name}, how are you?")


if __name__=="__main__":
    greet("admin")
