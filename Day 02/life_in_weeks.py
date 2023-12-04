# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years_left  = 90 - int(age)
weeks_left  = 52 * years_left
print(f"You have {weeks_left} weeks left. ")
