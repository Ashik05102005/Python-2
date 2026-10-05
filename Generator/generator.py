# def gen_fun ():
#     print("start")
#     yield 1

#     print("seccond call")
#     yield 2 

#     print("third call")
#     yield 3

# gen = gen_fun()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# def numbers():
#     for i in range(1, 7):
#         yield i

# nums = numbers()
# for i in range(1,10):
#     try:
#         print(next(nums))

#     except StopIteration :
#         print("error" )
#         break

# def gen() :
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# for num in gen():
#     print(num)


gen = (num**2 for num in range(10))
try :
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))

except StopIteration :
    print("limit exceeds")