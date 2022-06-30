def fun(x):

    y = x * x
    return y


global y
y = 0
fun(2)
print(y)
