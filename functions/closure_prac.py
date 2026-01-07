"""
This file holds the practice on Closure function
"""
def outer_function(name: str):
    fixed_value = 25
    def closure():
        print(f"name: {name}; fixed_value: {fixed_value}")
    return closure


if __name__ == "__main__":
    closure_obj = outer_function("Jane")
    print(closure_obj)
    # outer function is terminated; still the values enclosed in the outer function 
    # are remembered by the closure method
    closure_obj()
