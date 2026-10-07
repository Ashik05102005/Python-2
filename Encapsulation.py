class BankAccount :
    def __init__(self , account_holder , balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self , amount):
        self.__balance += amount

    def withdraw(self ,amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance



account = BankAccount ("Ashik", 10000)

account.deposit(2000)
account.withdraw(3000)

print(account.get_balance())

class Student :
    def __init__ (self , name ):
        self.name = name 
        self.__mark = 0
    
    def set_marks(self , mark):
        self.__mark = mark

    def get_marks(self ) :
        return self.__mark

student = Student("Ashik")

student.set_marks(85)

print(student.get_marks())


class Employee :
    def __init__(self , name , amount) :
        self.name = name 
        self.__salary = amount
    
    def set_salary (self , amount) :
        self.__salary = amount
    
    @property
    def get_salary (self):
        return self.__salary

employee = Employee("Ashik", 30000)

employee.set_salary(40000)

print(employee.get_salary)

