def decorator (func) :
    def wrapper() :
        print("start execution")
        func()
        print("finish execution")
    return wrapper

@decorator
def greet () :
    print("helloooo...")

greet()