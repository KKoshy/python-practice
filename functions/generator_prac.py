"""
This file holds the practice on generator operations
"""
import sys
import cProfile

def gen_number(num):
    while num >= 0:
        yield num
        num -= 1

def multi_yield():
    print("Experimenting multi yield")
    stat_01 = "At night, when the stars light up my room"
    yield stat_01
    stat_02 = "I sit by myself"
    yield stat_02

def starting_countdown():
    print("Initiating count down")
    for count in gen_number(10):
        print(f"{count} ... ")

def profile_memory():
    print("Profiling list comprehension - memory")
    nums_lc = [x for x in range(100)]
    print(nums_lc)
    print(sys.getsizeof(nums_lc))
    print("Profiling generator comprehension - memory")
    nums_gc = (x for x in range(100))
    print(nums_gc)
    print(sys.getsizeof(nums_gc))

def profile_speed():
    print("Profiling list comprehension - speed")
    print(cProfile.run("sum([x for x in range(1000)])"))
    print("Profiling generator comprehension - speed")
    # list comprehension generates values immediately; generator comprehension doesn't
    # using sum here to force the generator to generate values to be consumed
    # to be fair, using the sum for both list comprehension and generator comprehension
    print(cProfile.run("sum((x for x in range(1000)))"))



if __name__=="__main__":
    starting_countdown()
    start_value = int(input("Enter the start value: "))
    custom_count = gen_number(start_value)
    print(f"First count of {next(custom_count)}")
    second_value = next(custom_count)
    if second_value%2==0:
        print(f"Second count considered {second_value}")

    # generator expression/generator comprehension
    print("Creating a generator expression/generator comprehension")
    gen_obj = (x for x in range(100))
    print(gen_obj)
    print(next(gen_obj))
    print([x for x in gen_obj])
    print("Done")

    # profiling performance
    profile_memory()
    profile_speed()

    # multi yield
    first = multi_yield()
    print(first)
    print(next(first))
    print(next(first))
