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

#Write your code below this line 👇

choose = int( input( "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n") )
print("\n\n\n\n")
if choose==0:
	print(rock)
elif choose==1:
	print(paper)
else:
	print(scissors)

computer_choose = random.randint(0,2)

print("Computer choice \n \n \n \n ")

if computer_choose==0:
	print(rock)

elif computer_choose==1:
	print(paper)
else:
	print(scissors)

if choose ==0:
	if computer_choose==0:
		print("Better Luck Next Time")
	elif computer_choose==1:
		print("You Lose")
	elif computer_choose==2:
		print("You Won ")

elif choose ==1:
	if computer_choose==0:
		print("You Won ")
	elif computer_choose==1:
		print("Better Luck Next Time")
	elif computer_choose==2:
		print("You Lose")

else:
	if computer_choose==0:
		print("You Lose")
	elif computer_choose==1:
		print("You Won")
	elif computer_choose==2:
		print("Better Luck Next Time")