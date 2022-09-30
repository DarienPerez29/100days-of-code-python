print("====================")
print("|| TIP CALCULATOR ||")
print("====================\n")

total_bill = float(input("\nWhat was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? (10, 12, or 15) ")) / 100 + 1
people = int(input("How many people to split the bill? "))

final_total = round(total_bill * tip_percentage / people, 2)
final_total = "{:.2f}".format(final_total)

print(f"\nEach person should pay: ${final_total}")