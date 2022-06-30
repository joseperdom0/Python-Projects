dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}

v = dictionary['one']
print(v)

for k in range(len(dictionary)):
    v = dictionary[v]
    print(v)