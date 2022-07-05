upper_limit = int(input("Find Prime numbers before this number: "))
primes = 0
for i in range(2, upper_limit+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes += 1
        print(i)

print("# of Prime numbers:", primes)
