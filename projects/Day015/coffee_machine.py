import modules.machine_config as m_conf

# Init machine variables
run_machine = True
resources = m_conf.resources
money = m_conf.money
menu = m_conf.MENU


def print_resources():
    """Prints the values of the resources of the coffee machine in a
    formatted way."""
    print("\n========= GENERAL REPORT =========")
    print(f" Water: {resources['water']}ml")
    print(f" Milk: {resources['milk']}ml")
    print(f" Coffee: {resources['coffee']}g")
    print(f" Money: ${money}")
    print("=================================\n")


while run_machine:
    enough_resources = False

    # Init inserted coins
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    total_input = 0.0
    change = 0.0

    option = input(
        ">> What would you like? (espresso/latte/cappuccino): "
    ).lower()

    # ====== Turning off the machine ======
    if option == "off":
        print("Turing machine off...")
        run_machine = False

    # ====== Print report of the machine ======
    elif option == "report":
        print_resources()

    # ====== Main flow to make coffee ======
    elif option in menu.keys():
        ingredients = menu[option]["ingredients"]

        # Checking for resources
        for ingredient in ingredients:
            if ingredients[ingredient] <= resources[ingredient]:
                enough_resources = True
            else:
                print(f"Sorry, there is not enough {ingredient}.")

        # Flow if enough resources
        if enough_resources:
            option_cost = menu[option]['cost']
            print(f"\n{option.capitalize()} has a cost of ${option_cost}")

            # Capture inserted coins
            print(f"\nPlease insert coins...")
            quarters = int(input(">> How many quarters?: ")) * 0.01
            dimes = int(input(">> How many dimes?: ")) * 0.1
            nickels = int(input(">> How many nickels?: ")) * 0.5
            pennies = int(input(">> How many pennies?: ")) * 0.25
            total_input = quarters + dimes + nickels + pennies
            print(f"Your total: ${total_input}")

            # Check if money inserted is enough
            if total_input >= option_cost:
                change = total_input - option_cost
                print()

                if change > 0:
                    print(f"<< Here's your change: ${change}")

                # Update machine values
                for resource in resources:
                    if resource in ingredients.keys():
                        resources[resource] -= ingredients[resource]

                money += option_cost

                print(f"<< Here's your {option} ☕. Enjoy!\n")

            else:
                print("\nSorry, that's not enough money. Money refounded.\n")

    # ====== Invalid option ======
    else:
        print("\nPlease, select a valid option")
