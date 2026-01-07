"""
This file holds the practice on Advanced generator operations
"""
def infinite_number():
    num = 0
    while True:
        try:
            trigger = yield num
            if trigger: 
                num += 1
        except ValueError:
            yield "Handling exception"
        except GeneratorExit:
            # Important
            # no yield/print should be added after GeneratorExit
            # otherwise causes RuntimeError
            return "All Done"


if __name__ == "__main__":
    print("Initiating infinite number series")
    gen_obj = infinite_number()
    print(gen_obj)
    # prime the generator
    print(next(gen_obj))
    print(gen_obj.send(True))
    print(gen_obj.send(True))
    print(gen_obj.throw(ValueError))
    print(gen_obj.send(True))
    print(gen_obj.send(False))
    print(gen_obj.close())
    # next after closing causes StopIteration
    print(next(gen_obj))
    
