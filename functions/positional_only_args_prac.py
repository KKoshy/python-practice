"""
This file holds the practice on positional only arguments
"""
# all arguments left of / are positional only args
def do_something(a, b, /):
    print(f"Values are {a}, {b}")


def do_something_pos(a, b, /, name, org):
    print(f"Values are {a}, {b}, {name}, {org}")


if __name__=="__main__":
    do_something(3, 4)
    # Causes Type Error otherwise; 
    # TypeError: do_something_pos() got some positional-only arguments passed as keyword arguments: 'a, b'
    # do_something_pos(a=3, b=4, name='June', org='Autumn')
    do_something_pos(3, 4, name='June', org='Autumn')
