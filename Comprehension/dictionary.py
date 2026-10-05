# 🔵 Dictionary Comprehension
# 12. Number and Square

# Create a dictionary where the key is the number and the value is its square.

# For numbers from 1 to 5.

# Expected structure:

# {1: 1, 2: 4, ...}

squares = {num : num * num for num in range(1,6)}

print(squares)

# 13. Number and Cube

# Create a dictionary containing numbers from 1 to 10 as keys and their cubes as values.

cubes = {num : num ** 3 for num in range(1,11)}

print(cubes)

# 14. Even Number Dictionary

# Given:

# Create a dictionary containing only even numbers as keys and their squares as values.\

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_square = {num : num ** 2 for num in numbers if num % 2 == 0}

print(even_square)

# 15. Word Length

# Given:


# Create a dictionary where:

# key → word
# value → length of the word

words = ["python", "react", "html", "javascript"]

word_len = {word : len(word) for word in words }

print(word_len)

# 16. Character Frequency

# Given:


# Create a dictionary containing each character and its frequency.

# For example:

# {'p': 1, ...}

# Try to solve it using dictionary comprehension.

word = "programming"

freq = {char : word.count(char) for char in word}

print(freq)

# 17. Student Marks

# Given:

# Create a new dictionary containing only students who scored 50 or above.

students = {
    "Ashik": 85,
    "Rahul": 45,
    "Arun": 72,
    "Amal": 35,
    "John": 90
}

student_above_50 = {name : mark for name , mark in students.items() if mark > 50 }

print(student_above_50)