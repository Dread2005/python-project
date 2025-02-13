from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True

menu = Menu()
money_mach = MoneyMachine()
coffee_maker = CoffeeMaker()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like?{options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_mach.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(f"${drink.cost}")
        if money_mach.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


    
        



    


