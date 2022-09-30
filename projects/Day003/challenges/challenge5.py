# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
loveString = "love"
trueString = "true"
names = (name1 + name2).lower().replace(' ', '')
trueCounter = 0
loveCounter = 0
score = 0

for i in range(len(loveString)):
    loveCounter += names.count(loveString[i])
    trueCounter += names.count(trueString[i])

score = int(str(trueCounter) + str(loveCounter))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")