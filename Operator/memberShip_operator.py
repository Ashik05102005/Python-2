# Check Character
# word = "apple"
# if "a" in word:
#     print("a is presenet")
# else :
#     print("a is not in that")

# Check Item in List

# fruits = ["apple", "banana", "orange", "mango"]
# if "orange" in fruits :
#     print("orange is in the fruits")
# else :
#     print("orange is not in the fruits")

# Find Common Elements

# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 60, 70]
# common_list  = []

# for num  in list1  :
#     if(num in list2):
#         common_list.append(num)

# print(common_list)


# Check Allowed Username

# allowed_users = ["ashik", "admin", "john", "alex"]

# user_name = input("Enter user name : ")

# if(user_name in allowed_users) :
#     print("access granted")

# else :
#     print("access denied")


# 6. Find Common Characters

word1 = "programming"
word2 = "python"
common = []

for char in word1 :
    if (char in word2 or word1.count(char)>1 ) and char not in common :
        common.append(char)

print(common)