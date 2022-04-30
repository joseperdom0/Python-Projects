animals = {"sheep": 6769,
           "cow": 3848,
           "pig": 1296,
           "goat": 678,
           "chicken": 23,
           }
money = int(input())
purchased = False
for animal, price in animals.items():
    if money >= price:
        quantity = money // price
        purchased = True
        if quantity > 1:
            if animal != "sheep":
                print(f"{quantity} {animal}s")
            else:
                print(f"{quantity} {animal}")
            break
        else:
            print(f"{quantity} {animal}")
            break
if not purchased:
    print("None")
