# 5. Add Two Numbers

# Create a decorator that prints the result of a function.

# Given:

def add_decorator(func)  : 
    def wrapper(*args) :
        res = func(*args)
        return f"result : {res}"
    return wrapper

@add_decorator
def add(a, b):
    return a + b

print(add(10, 20))





# Expected:

# Result: 30


