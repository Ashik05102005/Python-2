def first_non_repeated(s):
    for char in s :
        if s.count(char) == 1 :
            return char

print(first_non_repeated("swiss"))