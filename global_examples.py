def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


def my_function2():
    global var2
    var2 = 2
    print("var2", var2)


var2 = 0
my_function2()
print("var2", var2)