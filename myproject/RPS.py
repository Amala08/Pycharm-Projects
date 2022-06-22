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


game_choice_list = [rock, paper, scissors]
user_choice = int(input("Enter your choice : 0 for Rock,  1 for Paper and 2 for Scissor\n"))
if user_choice >= 3:
    print("You enter a wrong number: You lost")
else:
    print(game_choice_list[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(game_choice_list[computer_choice])
    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice == 0:
        if computer_choice == 1:
            print("Computer win")
        else:
            print("You win")
    elif user_choice == 1:
        if computer_choice == 2:
            print("Computer win")
        else:
            print("You win")
    elif user_choice == 2:
        if computer_choice == 0:
            print("Computer win")
        else:
            print("You win")
