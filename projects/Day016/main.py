from modules.menu import Menu, MenuItem
from modules.coffee_maker import CoffeeMaker
from modules.money_machine import MoneyMachine

my_menu = Menu()
my_coffee_mkr = CoffeeMaker()
my_money_machine = MoneyMachine()

machine_running = True

while machine_running:
    command = input(
        ">> What would you like? (espresso/latte/cappuccino): ").lower()

    print()

    if command == "off":
        print("Turning machine off...")
        machine_running = False

    elif command == "report":
        my_coffee_mkr.report()
        my_money_machine.report()
        print()

    elif command in my_menu.get_items():
        ordered_drink = my_menu.find_drink(command)

        if my_coffee_mkr.is_resource_sufficient(ordered_drink):

            print("Sufficint resources. Asking for coins... [WIP]")

    else:
        print("Please insert a valid option...")
