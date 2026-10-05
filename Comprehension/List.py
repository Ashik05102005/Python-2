# 1. Squares

# Given:

# Create a list containing the squares of all numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_numbers = [num for num in numbers]

# 2. Even Numbers

# Given:

# Create a list containing only the even numbers.

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)

# 3. Positive Numbers

# Given:

# Create a list containing only positive numbers.

numbers = [-5, 10, -2, 8, -1, 15, 20]

pos_numbers = [num for num in numbers if num>0]

print(pos_numbers)


# 4. Words with Length Greater Than 4

# Given:

# Create a list containing only words whose length is greater than 4.

words = ["python", "java", "html", "javascript", "css", "react"]

len_gt_4 = [word for word in words if len(word)>4]

print(len_gt_4)


# 5. Convert to Uppercase

# Given:

# Create a list containing all words in uppercase.

words = ["python", "react", "javascript", "html"]

words_upper = [char.upper() for char in words]

print(words_upper)




# 6. Extract Vowels

# Create a list containing only the vowels.

word = "programming"
vowels = list("aeiou")
vowels_list = [char for char in word if char in vowels ]

print(vowels_list)