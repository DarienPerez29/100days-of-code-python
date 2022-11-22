############DEBUGGING#####################

# Describe Problem ###############################################
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

### SOLUTION
# 1. What is the for-loop doing?
#   It's iterating in a range from 1 to 20, but 20 is not included
# 2. When is the function meant to print "You got it"?
#   When 'i' is equal to 20
# 3. What are your assuptions about i?
#   'i' takes values from 1 to 19, but never 20, so the message
#   "You got it" never gets printed.
# A: Increment the max value of range to 21

# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

###################################################################

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

### SOLUTION
# The 'dice_num' variable stores the index of the element that 
# is going to be accesed in the 'dice_imgs' list, and it gets a 
# random number between 1 and 6, so the element at position 0
# nevet gets accesed, and the element at position 6 doesn't exists,
# so that's why it throws an error
# R: Change the range of the randint

# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

###################################################################

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

### SOLUTION
# Year 1994 it's not included in the if block
# R: Modify if or elif statement to include 1994 using
# <= or >=

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

###################################################################

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

### SOLUTION
# 1. Set the correct indentation of print line
# 2. Cast to int the age input variable
# 3. Turn string to f-string of print line

# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

###################################################################

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

### SOLUTION
# 'word_per_page' variable is using a logical operator instead of
# the assignment operator
# R: Change '==' to '='

pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

###################################################################

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])