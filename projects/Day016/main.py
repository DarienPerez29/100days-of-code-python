from modules.menu import Menu, MenuItem
from modules.coffee_maker import CoffeeMaker
from modules.money_machine import MoneyMachine

machine_running = True

while machine_running:
    command = input(">> What would you like? (espresso/latte/cappuccino):")
    if command == "off":
        print("\nTurning machine off...")
        machine_running = False
    else:
        print("\nPlease insert a valid option...")
