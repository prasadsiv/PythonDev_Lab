# You are going to write a program that will select a random name from a list of names. 
#The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.

# Line 1 splits the string names_string into individual names and puts them inside a List called names. 
#For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

#in Siv, Ben, Jenny, Michael, Chloe

names_string = input("Enter the names: ")
names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆

# #using random choice
# buyer = random.choice(names)
# print(f"{buyer} is going to buy the meal today!")
 
import random
person_number = random.randint(0, (len(names)-1))
buyer = names[person_number]
print(f"{buyer} is going to buy the meal today!")
 