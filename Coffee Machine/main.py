def resources_check():
    water_needed = MENU[User_choice]['ingredients']['water']
    milk_needed = MENU[User_choice]['ingredients']['milk']
    coffee_needed = MENU[User_choice]['ingredients']['coffee']

    water_available = resources['water']
    milk_available = resources['milk']
    coffee_available = resources['coffee']

    if water_available < water_needed:
        print("Sorry there is not enough water.")
        return False
    elif milk_available < milk_needed:
        print("Sorry there is not enough milk")
        return False
    elif coffee_available < coffee_needed:
        print("Sorry there is not enough coffee")
        return False
    else:
        return True


def update_resources():

    water_needed = MENU[User_choice]['ingredients']['water']
    milk_needed = MENU[User_choice]['ingredients']['milk']
    coffee_needed = MENU[User_choice]['ingredients']['coffee']

    resources['water'] -= water_needed
    resources['milk'] -= milk_needed
    resources['coffee'] -= coffee_needed
    resources['money'] += choice_cost


PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,
}
while True:
    User_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if User_choice == "report":
        print(f"""
        Water: {resources['water']}ml
        Milk: {resources['milk']}ml
        Coffee: {resources['coffee']}g
        Money: ${resources['money']}
        """)
        continue
    elif User_choice == "off":
        break

    if resources_check():
        print("Please insert coins.")
        nQuarters = int(input("how many quarters?: "))
        nDimes = int(input("how many dimes?: "))
        nNickels = int(input("how many nickles?: "))
        nPennies = int(input("how many pennies?: "))

        total_deposit = (QUARTER * nQuarters) + (DIME * nDimes) + (NICKEL * nNickels) + (PENNY * nPennies)
        choice_cost = MENU[User_choice]["cost"]

        if total_deposit == choice_cost:
            update_resources()
            print(f"Here is your {User_choice} ☕️. Enjoy!")
        elif total_deposit > choice_cost:
            update_resources()
            change = total_deposit - choice_cost
            print(f"Here is ${change} in change.")
            print(f"Here is your {User_choice} ☕️. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded.")
