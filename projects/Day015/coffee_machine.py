import modules.machine_config as m_conf

# Init machine variables
run_machine = True
resources = m_conf.resources
menu = m_conf.MENU


def print_resources():
    """Prints the values of the resources of the coffee machine in a
    formatted way."""
    print("\n====== RESOURCES REPORT =========")
    print(f" Water: {resources['water']}ml")
    print(f" Milk: {resources['milk']}ml")
    print(f" Coffee: {resources['coffee']}g")
    print(f" Money: ${resources['money']}")
    print("=================================\n")


while run_machine:
    option = input("What would you like? (espresso/latte/cappuccino):").lower()

    if option == "off":
        print("Turing machine off...")
        run_machine = False
    elif option == "report":
        print_resources()
    elif option in menu.keys():
        ingredients = menu[option]["ingredients"]

    else:
        print("\nPlease, select a valid option")
