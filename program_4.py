# Eliya Statema
# 2/12/25
# Bank Balance

budget_amount = int(input("Enter your budgeted amount for the month: "))
total = 0.0
expense = 1

while expense > 0:
    expense = int(input("Enter an expense or enter 0 to finish: "))
    while expense < 0:
        print("Error: You can not enter a negative number.")
        expense = int(input("Enter the correct expense amount: "))
    total += expense

difference = budget_amount - total

print(f"BUDGET AMOUNT: ${budget_amount}")
print(f"TOTAL EXPENSES: ${total:.2f}")
print(f"DIFFERENCE: ${difference:.2f}")
if difference < 0:
    print(f"You are ${abs(difference):.2f} over your budget.")
else:
    print(f"You are ${abs(difference):.2f} under your budget.")