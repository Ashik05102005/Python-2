# 7. Remove Duplicates

# Given:

# Create a set containing only unique numbers

numbers = [1, 2, 2, 3, 4, 4, 5, 5, 6]

num_set = {num for num in numbers}

print(num_set)



# 8. Unique Even Numbers

# Given:

# Create a set containing unique even numbers.

numbers = [1, 2, 2, 4, 5, 6, 6, 8, 9, 10, 10]

even_set = { num for num in numbers if num % 2 == 0 }

print(even_set)

# 9. Unique Word Lengths

# Given:

# Create a set containing the lengths of the words.


# Expected result should contain unique lengths.

words = ["cat", "dog", "apple", "banana", "car", "elephant"]

len_set = {len(word) for word in words}

print(len_set)

# 10. Unique Vowels

# Given:


# Create a set containing the unique vowels.

word = "programming programming"

vowels = list("aeiou")

vowels_set = { char for char in word if char in vowels}

print(vowels_set)


# 11. Numbers Divisible by 3

# Generate a set containing all numbers between 1 and 50 that are divisible by 3.

div_by3 = {num for num in range(1,50) if num % 3 == 0}

print(div_by3)

