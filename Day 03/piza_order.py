# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.

# Based on a user's order, work out their final bill.

# Small pizza (S): $15

# Medium pizza (M): $20

# Large pizza (L): $25

# Add pepperoni for small pizza (Y or N): +$2

# Add pepperoni for medium or large pizza (Y or N): +$3

# Add extra cheese for any size pizza (Y or N): +$1
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill =0 

if size.lower() == "s":
    bill+= 15
elif size.lower()== "m":
    bill+=20
elif size.lower() == "l":
    bill+=25;
else:
    print("Option not available")
if add_pepperoni.lower() =="y":
    if size.lower() == "s":
        bill+=2
    else:
        bill+=3
if extra_cheese.lower() == "y":
    bill+=1
print(f"Your final bill is: ${bill}")