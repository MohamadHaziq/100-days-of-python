import machine_data

MENU = machine_data.MENU
resources = machine_data.resources
coins = machine_data.coins


profit = 0

def is_resources_sufficient(ingredients):
    for resource in ingredients:
        if ingredients[resource] > resources[resource]:
            print (f"Sorry, not enough {resource}")
            return False  
    return True


def process_coins():
    ''' Process the total from coins inserted '''
    print ('Please insert coins')
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print (f"Here's your change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print ("That is insufficient money")
        return False

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print (f"Enjoy your {drink_name}\n")


is_on = True

while is_on == True:
    user_choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if user_choice == 'off':
        machine_status = False
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
