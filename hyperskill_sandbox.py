a = int(input())
b = int(input())

accumulate = 0
numbers = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        accumulate += i
        numbers += 1
print(accumulate / numbers)