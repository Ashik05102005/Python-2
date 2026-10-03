print("\nIn the case Immutable data")

a = 10
b = 10
print("\nin integers")
print(a is b)

a="hello"
b="hello"
print("\nin string")
print(a is b )


a = (1,2,3)
b = (1,2,3)
print("\nin tuple")
print(a is b)

print("\nIn the case Mutable data")

a = [1,2,3]
b = [1,2,3]
print("\nin list")
print(a is b)

a = {"name" : "Ashik" , "age" : 20}
b = {"name" : "Ashik" , "age" : 20}
print("\nin dictionary")
print(a is b )

a = {1,2,3,4}
b = {1,2,3,4}
print("\nin set")
print(a is b)

print(a is not b)