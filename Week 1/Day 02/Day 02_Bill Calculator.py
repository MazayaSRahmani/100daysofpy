print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10%, 20%, or 15%?\n"))
n_people = int(input("How many people to split the bill?\n"))

total_payment = (bill + bill*(tip/100))/n_people
print(f"Each person should pay: ${total_payment}")
