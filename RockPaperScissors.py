import random

rock='''
    _______
---'   ____)
      (____)
      (____)
      (____)
---.__(___)
'''

paper='''
    _______
---'   ____)____
          ______)
       __________)
      (__________)
---.__(________)
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




list=[rock, paper, scissors]
print("What do you choose? type in 0 for rock, 1 for paper and 2 for scissors.")
human_choice = input()
computer_choice=random.randint(0,2)

##print("You chose:"+ human_choice)
print("The computer chose: \n" + list[int(computer_choice)] + "You chose: \n" + list[int(human_choice)])

if human_choice==computer_choice:
    print("You have a draw.")
elif human_choice ==0 and computer_choice == 2:
    print("You won!")
elif int(human_choice) - int(computer_choice) == 1:
    print("You won!")
else:
    print("You lost!")
