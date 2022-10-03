import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!#$%&()*+"

print('''
=========================================
||| WELCOME TO THE PASSWORD GENERATOR |||
=========================================\n''')

n_letters = int(input("How many letters would you like in your password? "))
n_numbers = int(input("How many numbers would you like? "))
n_symbols = int(input("How many symbols would you like? "))

password = []

for i in range(n_letters):
    password.append(letters[random.randint(0, len(letters) - 1)])

for i in range(n_numbers):
    password.append(numbers[random.randint(0, len(numbers) - 1)])

for i in range(n_symbols):
    password.append(symbols[random.randint(0, len(symbols) - 1)])

password_s = []
for i in range(len(password)):
    randnum = random.randint(0, len(password) - 1)
    password_s.append(password[randnum])
    password.pop(randnum)

print(f"\n\nYour password is: {''.join(password_s)}")