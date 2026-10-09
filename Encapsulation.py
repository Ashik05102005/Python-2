# class BankAccount :
#     def __init__(self , account_holder , balance):
#         self.account_holder = account_holder
#         self.__balance = balance

#     def deposit(self , amount):
#         self.__balance += amount

#     def withdraw(self ,amount):
#         self.__balance -= amount

#     def get_balance(self):
#         return self.__balance



# account = BankAccount ("Ashik", 10000)

# account.deposit(2000)
# account.withdraw(3000)

# print(account.get_balance())

# class Student :
#     def __init__ (self , name ):
#         self.name = name 
#         self.__mark = 0
    
#     def set_marks(self , mark):
#         self.__mark = mark

#     def get_marks(self ) :
#         return self.__mark

# student = Student("Ashik")

# student.set_marks(85)

# print(student.get_marks())


# class Employee :
#     def __init__(self , name , amount) :
#         self.name = name 
#         self._salary = amount

#     @property
#     def salary (self):
#         return self._salary
    
#     @salary.setter
#     def salary(self , amount) :
#         if amount < 0:
#             raise ValueError("Salary cannot be negative")
#         self._salary = amount

#     # @salary.deleter
#     # def salary(self):
        

# employee = Employee("Ashik", 30000)


# employee.salary = 40000

# print(employee.salary)


class Person :
    def __init__(self , name ) :
        self.name = name
        self.__age = 0 

    @property
    def age (self):
        return self.__age

    @age.setter
    def age(self , age):
        if(age > 0 and age < 120) :
            self.__age = age
        else :
            print("Invalid Age")

    @age.deleter
    def age (self):
        print("deleting age")
        del self.__age

person = Person("Ashik")

person.age = 21


print(person.age)

del person.age
# print(person.age)