# Simple function
def greet():
    print("Hi")
    print("How do you do?")
    print("It's nice to see you again!")

# Function with one input
def greet_with_name(name):
    print(f"Hi {name}")
    print(f"How do you do {name}?")
    print(f"It's nice to see you again {name}!")

# Function with multiple inputs
def greet_with(name, location):
    print(f"Hi {name}")
    print(f"How do you do {name}?")
    print(f"It's nice to see you again {name} in {location}!")

# Function with multiple keyword arguments
def power_numbers(a, b):
    print(pow(a, b))

if __name__ == '__main__':
    greet_with("Darien", "Dubai")
    power_numbers(b = 2, a = 3)
    