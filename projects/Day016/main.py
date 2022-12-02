from modules.menu import Menu, MenuItem
from modules.coffee_maker import CoffeeMaker
from modules.money_machine import MoneyMachine

my_menu = Menu()
my_coffee_mkr = CoffeeMaker()
my_money_machine = MoneyMachine()

machine_running = True

while machine_running:
    command = input(">> What would you like? (espresso/latte/cappuccino): ")
    if command == "off":
        print("\nTurning machine off...")
        machine_running = False
    elif command == "report":
        my_coffee_mkr.report()
    else:
        print("\nPlease insert a valid option...")
