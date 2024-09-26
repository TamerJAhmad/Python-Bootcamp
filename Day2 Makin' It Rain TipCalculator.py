print("Welcome to the Makin' It Rain Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? ex. 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))

amountPerPerson = round((bill / people) * (1 + tip / 100),2)

print(f"Each person should pay: ${amountPerPerson}")