numbers = [1, 2, 3, 4, 5]

squares = {num : num**2 for num in numbers}

print(squares)

names = ["Alice", "Bob", "John"]
ages = [21, 25, 23]

details = {name : age for name,age in zip(names , ages)}

print(details)

even_nums = {num : num*num for num in range(1,11) if num%2 == 0}

print(even_nums)

students = {
    "Alice": 21,
    "Bob": 17,
    "John": 23,
    "David": 16,
    "Emma": 20
}

adult_students = {name : age for name,age in students.items() if age>=18}
print(adult_students)

celsius = {
    "Monday": 30,
    "Tuesday": 25,
    "Wednesday": 28
}

in_faranheat = {day : (cel * 9/5) + 32 for day,cel in celsius.items()}
print(in_faranheat)

words = ["apple", "banana", "cat", "elephant"]

words_len = {word : len(word) for word in words}
print(words_len)

students = {
    "student1": {"name": "John", "age": 21},
    "student2": {"name": "Alice", "age": 19},
    "student3": {"name": "Bob", "age": 23}
}

students_above20 = {name:{"name":value["name"] , "age" : value["age"]} for name , value in students.items() if value["age"]>=20}
print(students_above20)

word = "programming"
word_freq = {char : word.count(char) for char in word  }
print(word_freq)

students = {
    "Alice": 101,
    "Bob": 102,
    "John": 103
}

reversed_student = {value : key for key,value in students.items()}
print(reversed_student)

numbers = [1, 2, 3, 4, 5, 6]
odd_or_even = {num :"Even" if num%2 == 0 else "Odd" for num in numbers}
print(odd_or_even)

