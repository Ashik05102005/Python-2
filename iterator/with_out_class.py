
iterator = iter([num for num in range(1,40,3)])

while True :
    try : 
        print(next(iterator))

    except StopIteration :
        break