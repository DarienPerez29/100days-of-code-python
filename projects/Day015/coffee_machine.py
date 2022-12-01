# Init machine variables
run_machine = True
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


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
