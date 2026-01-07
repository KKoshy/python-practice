"""
This file holds the practice on print statement
"""

# printing with space padding
def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number+1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")


if __name__=="__main__":
    n = int(input("Enter the number: "))
    for i in range(1, n+1):
        # by default, print adds a new line after each call
        print(i, end="")

    # printing with decimal places
    print()
    marks = [40, 50, 60]
    print(f"{sum(marks)/len(marks):.2f}")
