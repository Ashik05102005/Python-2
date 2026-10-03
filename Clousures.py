def outer ():
    name = "Ashik" 
    def innner ():
        print(f"Welcome , {name}")

    return innner
fun = outer()
fun()