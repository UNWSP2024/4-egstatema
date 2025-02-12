# Eliya Statema
# 2/12/25
# Average Rainfall

print("This program will calculate the average amount of rainfall per month over a given amount of time.")

number_of_years = int(input("How many years? "))
total_rainfall = 0.0

for years in range(number_of_years):
    for months in range(number_of_years * 12):
        rainfall = float(input("How many inches of rain did you receive this month? "))
        while rainfall < 0:
            print("Error: You can not enter a negative number.")
            rainfall = int(input("Enter the correct amount of rainfall: "))
        total_rainfall += rainfall

average_per_month = total_rainfall / (number_of_years * 12)

print(f"Number of months: {number_of_years * 12}")
print(f"The total rainfall: {total_rainfall:.1f}")
print(f"The average rainfall per month: {average_per_month:.1f}")