class NumberRange : 
    def __init__(self , start , end , step):
        self.current  = start
        self.max = end 
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max :
            value = self.current
            self.current += self.step
            return value

        else :
            raise StopIteration

numbers = NumberRange(2, 10, 2)

for num in numbers :
    print(num)