
from random import randint
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

# # Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
user_input=int(input("you choose what? 0=rock,1=paper,2=scissors?\n"))
print("You choose:")
if user_input==0:
  print(rock)
elif user_input==1:
  print(paper)
elif user_input==2:
  print(scissors)
# elif user_input>=2 and user_input<=0:
#   print("Invalid input you loose!")


computer_input=randint(0,2)
print("Computer choose:")
if computer_input==0: 
  print(rock)
if computer_input==1:
  print(paper)
if computer_input==2:
  print(scissors)


if user_input==0 and computer_input==0:
  print("Match drawn")
elif user_input==0 and computer_input==1:
  print("you loose")
elif user_input==0 and computer_input==2:
  print("You win!")



if user_input==1 and computer_input==0:
  print("You win!")
elif user_input==1 and computer_input==1:
  print("Match drawn")
elif user_input==1 and computer_input==2:
  print("You loose!")

if user_input==2 and computer_input==0:
  print("You loose!")
elif user_input==2 and computer_input==1:
  print("You win!")
elif user_input==2 and computer_input==2:
  print("Match drawn")