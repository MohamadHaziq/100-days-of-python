from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
cash_register = MoneyMachine()

profit = 0

is_on = True

coffee_maker = CoffeeMaker()

while is_on == True:
    user_choice = input(f"What would you like? {MENU.get_items()}:\n")
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        print (coffee_maker.report())
        print (cash_register.report())
    else:
        drink = MENU.find_drink(user_choice)
        # print (drink.ingredients)
        if coffee_maker.is_resource_sufficient(drink):
            if cash_register.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


