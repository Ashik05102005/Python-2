print("--- Enumerate ---\n")
fruits = ["apple", "banana", "orange", "mango"]

for index , fruit  in enumerate(fruits):
    print(index , fruit)
    
print("---------------------")


# 2. Start Index from 1

students = ["Ashik", "Rahul", "John", "Amal"]

for index , name in enumerate(students , 1 ) :
    print(index , name )
    
print("---------------------")

# 3. Find the Index of a Specific Item
numbers = [10, 25, 30, 45, 50]

# Use enumerate() to find the index of 45.

for index , num in enumerate(numbers):
    if(num == 45):
        print(f"index : {index}")

print("---------------------")

# 4. Print Even Numbers with Their Index

numbers = [10, 15, 20, 25, 30, 35, 40]

for index , num in enumerate(numbers) :
    
    if num % 2 == 0 :
        print(index , num)
        
print("---------------------")

# 5. Find the Position of a Student

students = ["Rahul", "Anu", "Ashik", "John", "Meera"]

for index , name in enumerate(students):
    if name == "Ashik" :
        print( f"{name} is at position 2")
# Ashik is at position 2

print("---------------------")

# 6. Modify Items Using Index

# Given:

numbers = [10, 20, 30, 40, 50]

for index , num in enumerate(numbers):
    numbers[index] = num * index


print(numbers)
print("---------------------")


print("\n-------- Zip --------")

# 7. Combine Two Lists
names = ["Ashik", "Rahul", "John"]
ages = [22, 24, 21]

for name , age in zip(names , ages) :
    print(name , age)

print("---------------------")


# 8. Create a Dictionary
keys = ["name", "age", "city"]
values = ["Ashik", 22, "Kozhikode"]

eg_dict = { key : value for key , value in zip(keys , values)}

print(eg_dict)

print("---------------------")


# 9. Calculate Total Marks
subjects = ["Math", "English", "Science"]
marks = [80, 75, 90]

for subject , mark in zip(subjects , marks):
    print( f"{subject} : {mark} ")

print(f"\nTotal : {sum(marks)} ")
print("---------------------")


# 10. Find Students Who Passed
names = ["Ashik", "Rahul", "John", "Amal"]
marks = [85, 35, 72, 28]

for name , mark in zip(names , marks) :
    if(mark > 50):
        print(name , mark)

print("---------------------")









