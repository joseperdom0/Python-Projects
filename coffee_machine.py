MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = {"q": .25,
         "d": .1,
         "n": .05,
         "p": .01}


def process_payment(ordered_drink, resources_left):
    enough_money = False
    price = MENU[ordered_drink]["cost"]
    print(price)
    inserted_money = 0
    exiting = False
    while not enough_money and not exiting:
        coin = input("""Please introduce coins: 
        q for Quarters($0.25)
        d for Dimes   ($0.10)
        n for Nickles ($0.05)
        p for Pennies ($0.01)
        or x to QUIT
        
        """)
        for key in money:
            if coin == key:
                inserted_money += money[key]
                print(f"Inserted money: {'{0:.3g}'.format(inserted_money)}")
        if inserted_money >= price:
            enough_money = True
            exiting = True
            resources_left["money"] += price
            print(f"Returning: {'{0:.3g}'.format(inserted_money-price)}")
    return enough_money, resources_left


def check_ingredients(ordered_drink, resources_left):
    enough_ingredients = True
    missing_ingredient = ""
    for key in MENU[ordered_drink]["ingredients"]:
        if (resources_left[key]) > MENU[ordered_drink]["ingredients"][key]:
            print("enough")
        else:
            print("not enough")
            missing_ingredient = key
            enough_ingredients = False
    return enough_ingredients, missing_ingredient


def make_drink(ordered_drink, resources_left):
    for key in MENU[ordered_drink]["ingredients"]:
        resources_left[key] -= MENU[ordered_drink]["ingredients"][key]
    print(f"Enjoy your {ordered_drink}")
    return resources_left


def report(resources_left):
    for key in resources_left:
        print(f"{key.title()} left = {resources[key]}")


turned_on = True
resources["money"] = 0
while turned_on:
    order = input('What would you like? (espresso/latte/cappuccino)')
    if order == 'report':
        report(resources)
    elif order == 'espresso' or order == "latte" or order == "cappuccino":
        sufficient_ingredients, missing = (check_ingredients(order, resources))
        if sufficient_ingredients:
            if process_payment(order,resources):
                resources = make_drink(order, resources)
                print(resources)
            else:
                print("not enough money, returning coins")
        else:
            print(f"Sorry, we do not have enough {missing} to prepare your drink")
    if order == "off":
        turned_on = False
        print("Shutting down machine...")
