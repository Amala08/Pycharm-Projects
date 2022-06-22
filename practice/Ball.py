import random
red = -1
white = 0
black = "Out"
yellow = 5
green = 1
players = int(input("how many Players are going to play: "))
balls = [red,white,black,yellow,green]
rounds = random.choice(balls)
print(f"In this round you selected {rounds} ball")
score = 0
for score in balls:
    if rounds == red:
        score += red
    if rounds == white:
        score += white
    if rounds == yellow:
        score += yellow
    if rounds == green:
        score += green
    if rounds == black:
        print("You are Out")
        break
print(score)