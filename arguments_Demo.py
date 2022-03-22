def my_function(*args):
    for n in args:
        print(n)

def sum_function(*args):
    return sum(args)


my_function("1","perro","casa")
print(sum_function(1,2,3,4,4,6))