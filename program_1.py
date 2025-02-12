# Eliya Statema
# 2/12/25
# Movie Tickets

total = 0
keep_going = "Y"

while keep_going == "Y":
    input("Enter the name of the movie: ")
    number = int(input("How many tickets would you like to purchase for this movie? "))
    while number < 0:
        print("Error: You can not enter a negative number.")
        number = int(input("Enter the correct number of tickets would you like to purchase for this movie: "))
    total += number
    keep_going = input('''Are there more movies you would 
like to purchase tickets for? (Y/N) ''')

print(f"Total number of tickets: {total}")