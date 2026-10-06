from functools import reduce

# ------------- MAP -----------------

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda num : num * num  , numbers))

print(squares)

words = ["python", "react", "javascript", "html"]

to_upper_case = list(map(lambda word : word.upper() , words))

print(to_upper_case)

words = ["apple", "banana", "cat", "elephant"]

length_of_words = list(map(lambda word : len(word) , words))

print(length_of_words)

# ------------------- Filter ------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda num : num % 2 == 0 , numbers))

print(even)

numbers = [10, 15, 20, 25, 30, 35, 40]

odd = list(filter(lambda num : num % 2 == 1 , numbers))

print(odd)

words = ["cat", "elephant", "dog", "python", "hi", "javascript"]

len_gt_5 = list(filter(lambda word : len(word)>=5 ,words))

print(len_gt_5)

# ------------------- Reduce ------------------

numbers = [10, 20, 30, 40, 50]

sum = reduce(lambda a,b : a + b , numbers)

print(sum)

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda a,b : a * b , numbers)

print(product)

numbers = [25, 10, 75, 40, 90, 15]

largest = reduce(lambda a,b : a if a > b else b , numbers)

print(largest)

smallest = reduce(lambda a,b : a if a < b else b , numbers)

print(smallest)

words = ["Python", "is", "very", "powerful"]

single_string = reduce(lambda a,b : a+ " " +b , words)

print(single_string)


# ---------- Combined ------------

numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda num : num % 2 == 0 , numbers))

squares = list(map(lambda num : num * num , even))

sum = reduce(lambda a,b : a + b , squares)

# print(squares)
print(sum)

salaries = [25000, 40000, 18000, 55000, 30000, 15000]

gt_25000 = list(filter(lambda salary : salary > 25000 , salaries))

icreased_by_5000 = list(map(lambda salary : salary + 5000 , salaries ))

total_salary = reduce(lambda a , b : a + b , salaries )

print(total_salary)