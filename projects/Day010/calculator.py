import art
# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

# Print logo
print(art.logo)

# Get number 1
num1 = float(input("What's the first number?: "))

calculate = True
while calculate:
    # Get symbol
    operation_menu = "Pick an operation: ("
    for sym in operations:
        operation_menu += f"{sym}, "

    operation_menu = operation_menu[:-2] + "): "
    
    # Validate symbol is correct
    ask_valid_operation = True
    while ask_valid_operation:
        symbol = input(operation_menu)
        if symbol in operations:
            ask_valid_operation = False
        else:
            print("\nPlease, select a valid operation...")

    # Get next number
    num2 = float(input("What's the next number?: "))

    # Calculate result
    result = operations[symbol](num1, num2)

    # Print result
    print(f"{num1} {symbol} {num2} = {result}\n")

    # Ask for an extra operation
    ask_extra_operation = True
    while ask_extra_operation:
        option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")
        if option == "n":
            calculate = False
            ask_extra_operation = False
            print("Bye...")
        elif option == "y":
            num1 = result
            ask_extra_operation = False
        else:
            print("Please, select a valid option...")
