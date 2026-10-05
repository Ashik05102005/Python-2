# gen = ( num for num in range(1,101) if num%5 == 0   )

# flag = 1

# while flag == 1 :
#     try :
#         print(next(gen))
#         flag = int(input("if you want the next number (0/1) : "))
#     except StopIteration:
#         print("limit exceeds")
#         break 
    

# Positive Numbers
# Given a list:

# numbers = [-5, 10, -2, 8, 0, -7, 15]

# gen = (num for num in numbers if num>0 )



# Even Numbers from List
# Given:

# numbers = [12, 5, 8, 21, 30, 17, 44]

# gen = (num for num in numbers if num % 2 == 0)

# Vowels
# Given:

# word = "programming"
# vowels = list("aeiou")

# def Gen () :
#     for char in word :
#         if char in vowels :
#             yield char

# for char in Gen():
#     print(char)


