import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")


# import random
# game = [rock,paper,scissors]
# computer_chose = random.randint(0,2)
# user_choice = int(input("What do you choose ? Type 0 for Rock , 1 for Paper or 2 for Scissors "))
# if user_choice > 2 or user_choice < 0:
#     print("No option available")
#     exit()
# else:
#     print(game[user_choice])
#     print("Computer chose:")
#     print(game[computer_chose])
# if user_choice == computer_chose:
#     print("it's a draw")
#     exit()
# match user_choice:
#     case 0:
#         if computer_chose == 2:
#             print("You Win!")
#         else:
#             print("You lose")
#     case 2:
#         if computer_chose == 1:
#             print("You Win!")
#         else:
#             print("You lose")
#     case 1:
#          if computer_chose == 0:
#             print("You Win!")
#          else:
#             print("You lose")
#     case _:
#         print("You lose")