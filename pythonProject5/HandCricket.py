#Hand Cricket Game
import random
overs = int(input("How many overs you like to play: "))
o = overs * 6
you = input("Choose Even or Odd : ")
num = int(input("Enter number between 0 to 6 :"))
computer = random.randint(0,7)
print(f"Computer = {computer}")
x = num + computer
toss = ["Batting", "Bowling"]
if you == "Even":
    if x % 2 == 0:
        print("You won the Toss ")
        user = int(input("Choose 0 for Batting and 1 for Bowling :"))
        user_selected = toss[user]
        print(f"You opted for {user_selected} ")
        if user_selected == toss[0]:
            user_score = 0
            for score in range(1,o):
                run = int(input("Enter the num between 0 to 6: "))
                computer_run = random.randint(0,6)
                print(f"player run = {run}")
                print(f"Computer run = {computer_run}")
                if run != computer_run:
                    user_score = user_score + run
                    print(f"Player score = {user_score}")
                    continue
                else:
                    print("You are Out")
                    break
            computer_score = 0
            for score in range(1,o):
                computer_run = random.randint(0, 6)
                run = int(input("Enter the num between 0 to 6: "))
                print(f"Computer run = {computer_run}")
                print(f"player run = {run}")
                if run != computer_run:
                    computer_score = computer_score + computer_run
                    print(f"Computer score = {computer_score}")
                    if user_score > computer_score:
                        continue
                    else:
                        break
                else:
                    print("Computer Out")
                    break
            if user_score > computer_score:
                print("You Won the Match")
            elif user_score < computer_score:
                print("Computer Won the Match")
            else:
                user_score = computer_score
                print("Match is Tie")
        else:
            user_selected == toss[1]
            computer_score = 0
            for score in range(1,o):
                computer_run = random.randint(0, 6)
                run = int(input("Enter the num between 0 to 6: "))
                print(f"Computer run = {computer_run}")
                print(f"player run = {run}")
                if run != computer_run:
                    computer_score = computer_score + computer_run
                    print(f"Computer score = {computer_score}")
                    continue
                else:
                    print("Computer Out")
                    break
            user_score = 0
            for score in range(1,o):
                run = int(input("Enter the num between 0 to 6: "))
                computer_run = random.randint(0, 7)
                print(f"player run = {run}")
                print(f"Computer run = {computer_run}")
                if run != computer_run:
                    user_score = user_score + run
                    print(f"Player score = {user_score}")
                    if user_score < computer_score:
                        continue
                    else:
                        break
                else:
                    print("You are Out")
                    break
            if user_score > computer_score:
                print("You Won the Match")
            elif user_score < computer_score:
                print("Computer Won the Match")
            else:
                user_score = computer_score
                print("Match is Tie")
    else:
        print("Computer won the toss")
        machine = random.randint(0,1)
        comp_selected = toss[machine]
        print(f"Computer opted for {comp_selected}")
        if comp_selected == toss[1]:
                    user_score = 0
                    for score in range(1,o):
                        run = int(input("Enter the num between 0 to 6: "))
                        computer_run = random.randint(0,6)
                        print(f"player run = {run}")
                        print(f"Computer run = {computer_run}")
                        if run != computer_run:
                            user_score = user_score + run
                            print(f"Player score = {user_score}")
                            continue
                        else:
                            print("You are Out")
                            break
                    computer_score = 0
                    for score in range(1,o):
                        computer_run = random.randint(0, 6)
                        run = int(input("Enter the num between 0 to 6: "))
                        print(f"Computer run = {computer_run}")
                        print(f"player run = {run}")
                        if run != computer_run:
                            computer_score = computer_score + computer_run
                            print(f"Computer score = {computer_score}")
                            if user_score > computer_score:
                                continue
                            else:
                                break
                        else:
                            print("Computer Out")
                            break
                    if user_score > computer_score:
                        print("You Won the Match")
                    elif user_score < computer_score:
                        print("Computer Won the Match")
                    else:
                        user_score = computer_score
                        print("Match is Tie")
        else:
            comp_selected == toss[0]
            computer_score = 0
            for score in range(1,o):
                computer_run = random.randint(0, 6)
                run = int(input("Enter the num between 0 to 6: "))
                print(f"Computer run = {computer_run}")
                print(f"player run = {run}")
                if run != computer_run:
                    computer_score = computer_score + computer_run
                    print(f"Computer score = {computer_score}")
                    continue
                else:
                    print("Computer Out")
                    break
            user_score = 0
            for score in range(1,o):
                run = int(input("Enter the num between 0 to 6: "))
                computer_run = random.randint(0,6)
                print(f"player run = {run}")
                print(f"Computer run = {computer_run}")
                if run != computer_run:
                    user_score = user_score + run
                    print(f"Player score = {user_score}")
                    if user_score < computer_score:
                        continue
                    else:
                        break
                else:
                    print("You are Out")
                    break
            if user_score > computer_score:
                print("You Won the Match")
            elif user_score < computer_score:
                print("Computer Won the Match")
            else:
                user_score = computer_score
                print("Match is Tie")
else:
    you == "Odd"
    if x % 2 != 0:
        print("You won the Toss ")
        user = int(input("Choose 0 for Batting and 1 for Bowling :"))
        user_selected = toss[user]
        print(f"You opted for {user_selected} ")
        if user_selected == toss[0]:
            user_score = 0
            for score in range(1,o):
                run = int(input("Enter the num between 0 to 6: "))
                computer_run = random.randint(0,6)
                print(f"player run = {run}")
                print(f"Computer run = {computer_run}")
                if run != computer_run:
                    user_score = user_score + run
                    print(f"Player score = {user_score}")
                    continue
                else:
                    print("You are Out")
                    break
            computer_score = 0
            for score in range(1,o):
                computer_run = random.randint(0, 6)
                run = int(input("Enter the num between 0 to 6: "))
                print(f"Computer run = {computer_run}")
                print(f"player run = {run}")
                if run != computer_run:
                    computer_score = computer_score + computer_run
                    print(f"Computer score = {computer_score}")
                    if user_score > computer_score:
                        continue
                    else:
                        break
                else:
                    print("Computer Out")
                    break
            if user_score > computer_score:
                print("You Won the Match")
            elif user_score < computer_score:
                print("Computer Won the Match")
            else:
                user_score = computer_score
                print("Match is Tie")
        else:
            user_selected == toss[1]
            computer_score = 0
            for score in range(1,o):
                computer_run = random.randint(0, 6)
                run = int(input("Enter the num between 0 to 6: "))
                print(f"Computer run = {computer_run}")
                print(f"player run = {run}")
                if run != computer_run:
                    computer_score = computer_score + computer_run
                    print(f"Computer score = {computer_score}")
                    continue
                else:
                    print("Computer Out")
                    break
            user_score = 0
            for score in range(1,o):
                run = int(input("Enter the num between 0 to 6: "))
                computer_run = random.randint(0,6)
                print(f"player run = {run}")
                print(f"Computer run = {computer_run}")
                if run != computer_run:
                    user_score = user_score + run
                    print(f"Player score = {user_score}")
                    if user_score < computer_score:
                        continue
                    else:
                        break
                else:
                    print("You are Out")
                    break
            if user_score > computer_score:
                print("You Won the Match")
            elif user_score < computer_score:
                print("Computer Won the Match")
            else:
                user_score = computer_score
                print("Match is Tie")
    else:
        print("Computer won the toss")
        machine = random.randint(0,1)
        comp_selected = toss[machine]
        print(f"Computer opted for {comp_selected} ")
        if comp_selected == toss[1]:
                    user_score = 0
                    for score in range(1,o):
                        run = int(input("Enter the num between 0 to 6: "))
                        computer_run = random.randint(0,6)
                        print(f"player run = {run}")
                        print(f"Computer run = {computer_run}")
                        if run != computer_run:
                            user_score = user_score + run
                            print(f"Player score = {user_score}")
                            continue
                        else:
                            print("You are Out")
                            break
                    computer_score = 0
                    for score in range(31):
                        computer_run = random.randint(0, 6)
                        run = int(input("Enter the num between 0 to 6: "))
                        print(f"Computer run = {computer_run}")
                        print(f"player run = {run}")
                        if run != computer_run:
                            computer_score = computer_score + computer_run
                            print(f"Computer score = {computer_score}")
                            if user_score > computer_score:
                                continue
                            else:
                                break
                        else:
                            print("Computer Out")
                            break
                    if user_score > computer_score:
                        print("You Won the Match")
                    elif user_score < computer_score:
                        print("Computer Won the Match")
                    else:
                        user_score = computer_score
                        print("Match is Tie")
        else:
            comp_selected == toss[0]
            computer_score = 0
            for score in range(1,o):
                computer_run = random.randint(0, 6)
                run = int(input("Enter the num between 0 to 6: "))
                print(f"Computer run = {computer_run}")
                print(f"player run = {run}")
                if run != computer_run:
                    computer_score = computer_score + computer_run
                    print(f"Computer score = {computer_score}")
                    continue
                else:
                    print("Computer Out")
                    break
            user_score = 0
            for score in range(1,o):
                run = int(input("Enter the num between 0 to 6: "))
                computer_run = random.randint(0,6)
                print(f"player run = {run}")
                print(f"Computer run = {computer_run}")
                if run != computer_run:
                    user_score = user_score + run
                    print(f"Total score = {user_score}")
                    if user_score < computer_score:
                        continue
                    else:
                        break
                else:
                    print("You are Out")
                    break
            if user_score > computer_score:
                print("You Won the Match")
            elif user_score < computer_score:
                print("Computer Won the Match")
            else:
                user_score = computer_score
                print("Match is Tie")



