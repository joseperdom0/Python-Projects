def prime_checker(number):
    is_prime = True
    for dividend in range(2, number):
        if number % dividend == 0:
            is_prime = False
    print(f"{number} is prime = {is_prime}")


n = int(input("Check this number: "))
prime_checker(number=n)
