import random
rock='''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors='''
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list=[rock, paper, scissors]
computer_choice=random.randint(0,2)
user_choice=int(input("what do you choose? TYpe 0 for Rock, 1 for paper or 2 for scissors."))
print("Your chose:" + list[user_choice])
print("computer chose:" + list[computer_choice])

if user_choice == 0:
    if computer_choice == 2:
        print("You win")
    elif computer_choice == 1:
        print("You lose")
    else:
        print("draw")
elif user_choice == 1:
    if computer_choice == 0:
        print("You win")
    elif computer_choice == 2:
        print("You lose") 
    else:
        print("draw")
elif user_choice == 2:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
    else:
        print("draw")


