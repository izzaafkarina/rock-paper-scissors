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
import random

image = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user > 2 or user < 0:
	print("Invalid input")
else:
	print(image[user])

	computer = random.randint(0,2)
	print("computer choose:")
	print(image[computer])
	
	if user == 0 and computer == 2:
		print("You win :)")
	elif computer == 0 and user == 2:
		print("You lose :(")
	elif user == computer:
		print("It's a draw")
	elif user > computer:
		print("You win :)")
	elif computer > user:
		print("You lose :(")
