foo = set()
for i in range(42):
    foo.add('cake')

foo.add('hello')
foo.add('world')

print(len(foo))
print(foo)

x_coordinate = (42,)

print(type(x_coordinate))