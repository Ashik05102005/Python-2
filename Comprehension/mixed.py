
# Create three different collections using comprehension:

# List → squares of all numbers
# Set → squares of even numbers
# Dictionary → {number: cube} for numbers greater than 5


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [num**2 for num in numbers ]

print(squares)

even_squares = {num**2 for num in numbers if num % 2 == 0}

print(even_squares)

dict_cube = {num : num ** 3 for num in numbers if num > 5 }

