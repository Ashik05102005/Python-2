class Number :
    def __init__ (self , max):
        self.current = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max :
            value = self.current
            self.current += 1
            return value
        else :
            raise StopIteration

number = Number(10)

for num in number :
    print(num)

