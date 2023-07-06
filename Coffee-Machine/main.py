from art import logo
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coins():
    """returns total calculated from coins inserted"""
    print("Please enter coins.")
    quarters = float(input("How many quarters?: "))
    nickles = float(input("How many nickles?: "))
    dime = float(input("How many dime?: "))
    pennies = float(input("How many pennies?: "))
    total = quarters * 0.25 + dime * 0.1 + nickles * 0.05 + pennies * 0.01
    a = MENU[choice]
    cost_of_drink = a["cost"]
    if total >= cost_of_drink:
        change = round(total - cost_of_drink, 2)
        print(f"Here is your change of ${change}")
        print("Enjoy your drink!!! ☕️ ")
        return True
    else:
        print("Sorry, you do not have enough money, Money refunded")
        return False





def sufficency(order_ingredients):
    """Returns boolean if sufficency is satisfied"""

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True



def report():
    water_level = resources["water"]
    milk_level = resources["milk"]
    coffee_level = resources["coffee"]

    return f"Water: {water_level}ml \nMilk: {milk_level}ml \nCoffee: {coffee_level}g \nProfit: ${profit}"


is_on = True
print(logo)
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)?: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(report())
    else:
        drink = MENU[choice]
        if sufficency(drink["ingredients"]):
           if coins():
               profit += drink["cost"]
               for i in resources:
                   ing = drink["ingredients"]
                   resources[i] -= ing[i]
           else:
               is_on = False
        else:
            is_on = False






