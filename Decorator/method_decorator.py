
def calc_decorator (func):
    def wrapper(*args , **kwargs):
        print("\n----------------------------\n")
        print("Calling" , func.__name__)
        res = func(*args,**kwargs)
        return f"result : {res}"
    return wrapper


class Calculator :

    @calc_decorator
    def addition(self,a,b):
        return a+b

    @calc_decorator
    def substract(self,a,b):
        return a-b

    @calc_decorator
    def multiply(self,a,b):
        return a*b

    @calc_decorator
    def divide(self,a,b):
        return a/b

calc = Calculator()
print(calc.addition(5,6))
print(calc.substract(5,6))
print(calc.multiply(5,6))
print(calc.divide(5,6))
print("\n----------------------------\n")