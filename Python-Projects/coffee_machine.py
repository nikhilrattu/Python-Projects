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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def check_resources():
    return (f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: ${money}\n")

def is_resources_sufficient(order_ingredients):
    '''returns True when order can be made, False if ingredients are insufficient'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    '''returns teh total calculated from coins inserted'''
    print("Insert coins")
    total=int(input("How  many quarters?"))*0.25
    total+=int(input("How  many dimes?"))*0.10
    total+= int(input("How  many nickels?")) * 0.05
    total+= int(input("How  many pennies?")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    '''returns True when money_received is enough to make a drink,
    and returns false when money is insufficient'''
    if money_received < drink_cost:
        print(f"Sorry that is not enough money. Money refunded")
        return False
    else:
        global money
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change")
        money += change
        return True

def make_coffee(drink_name, order_ingredients):
    '''deduct the required ingredients from the resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")
should_cont=True

while should_cont:
    ask_user=input("what would you like? (espresso/latte/cappuccino): ").lower().strip()
    if ask_user == "off":
        should_cont = False
    elif ask_user == "report":
        print(check_resources())

    else:
        drink = MENU[ask_user]
        if is_resources_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(ask_user, drink["ingredients"])

