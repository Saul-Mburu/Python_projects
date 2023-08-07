import random

while True:
    items = ["ROCK","PAPER","SCISSORS"]
    ai = random.choice(items)
    user = None

    while user not in items:
        user=input("rock, paper or scissors: ").upper()

    if user == ai:
        print(f"computer: , {ai}")
        print(f"Player: {user}")
        print("Outcome: !!!!Draw!!!!")
    elif user == "ROCK":
        if ai == "PAPER":
            print(f"computer: , {ai}")
            print(f"Player: {user}")
            print("Outcome: !!!!You Lose!!!!")
        if ai == "SCISSORS":
            print(f"computer: , {ai}")
            print(f"Player: {user}")
            print("Outcome: !!!!You Win!!!!")
    elif user == "SCISSORS":
        if ai == "PAPER":
            print(f"computer: , {ai}")
            print(f"Player: {user}")
            print("Outcome: !!!!You Win!!!!")
        if ai == "ROCK":
            print(f"computer: , {ai}")
            print(f"Player: {user}")
            print("Outcome: !!!!You Lose!!!!")
    elif user == "PAPER":
        if ai == "SCISSORS":
            print(f"computer: , {ai}")
            print(f"Player: {user}")
            print("Outcome: !!!!You Lose!!!!")
        if ai == "ROCK":
            print(f"computer: , {ai}")
            print(f"Player: {user}")
            print("Outcome: !!!!You Win!!!!")
    retry = input("Do you want to play again? Y/N: ").upper()
    if retry != "Y":
        break 
print("Thank you for playing")



