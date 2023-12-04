print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
split_bill = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10,12, or 15? "))
bill = bill / split_bill
tip =( bill * tip )/100
total_bill = bill +  tip
print(f"Each person should pay: ${total_bill:.2f}")