# Generate Numbers
# Create a generator that generates numbers from 1 to 10.


# def Gen():
#     for i in range(1,11):
#         yield i
# gen = Gen()


# Even Numbers
# Create a generator that generates all even numbers from 1 to 50.

# gen = (num for num in range(1,51) if num%2 == 0)


# Odd Numbers
# Create a generator that generates all odd numbers from 1 to 50.
# Squares

# gen = ( num for num in range(1,50) if num%2 == 1)

# Create a generator that generates the squares of numbers from 1 to 10.

# gen = (num*num for num in range(1,11))

# Countdown
# Create a generator that generates numbers from 10 down to 1.

gen = (num for num in range(10,0,-1))




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