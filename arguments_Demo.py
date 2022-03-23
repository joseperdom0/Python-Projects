def my_function(*args):
    for n in args:
        print(n)

def sum_function(*args):
    return sum(args)


def calculate(n,**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)
    n+= kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

my_function("1","perro","casa")
print(sum_function(1,2,3,4,4,6))

calculate(2, add=1, multiply=3)

class Car:

    def __init__(self, **kwargs):
        # if the keyword argument does not exist it will crash
        #self.make = kwargs["make"]
        #self.model = kwargs["model"]
        #instead we use
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")

my_car = Car(model="GT-R")
print(my_car.make)
