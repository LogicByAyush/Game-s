#Rock Paper Seissors
import random

def win(ch):
    print(f"It {ch} \nYou Win!!")
    return

def draw(ch):
    print(f"It {ch} too \n---DRAW---")
    return

def loss(ch):
    print(f"It {ch} \nYou Loss")
    return

player = input("Enter Your name: ")
choice = input("R for Rock\nP for Paper\nS for Seissors\nEnter you choice (R\P\s): ").lower()

random_ = random.randint(1, 3) 

if random_ == 1:
        random_ = "Rock"
        if choice == "s":
            win(random_)
        elif choice == "r":
            draw(random_)
        else:
            loss(random_)
elif random_ == 2:
        random_ = "Paper"
        if choice == "r":
            win(random_)
        elif choice == "p":
            draw(random_)
        else:
            loss(random_)
else:
        random_ = "Seissors"
        if choice == "p":
            win(random_)
        if choice == "s":
            draw(random_)
        else:
            loss(random_)