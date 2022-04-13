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

#Write your code below this line 👇
game_image = [rock, paper, scissors]
import random
Your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))
print(game_image[Your_choice])
Computer_choice = random.randint(0, 2)
print("Computer chose:\n" + game_image[Computer_choice])


if Your_choice == Computer_choice:
	print("It's a Drow!")

elif Your_choice == 0 and Computer_choice == 1:
	print("You Lose!")

elif Your_choice == 0 and Computer_choice == 2:
	print("You Win!")

elif Your_choice == 1 and Computer_choice == 2:
	print("You Lose!")



elif Your_choice == 1 and Computer_choice == 0:
	print("You Win!")

elif Your_choice == 2 and Computer_choice == 0:
	print("You Lose!")

elif Your_choice == 2 and Computer_choice == 1:
	print("You Win!")