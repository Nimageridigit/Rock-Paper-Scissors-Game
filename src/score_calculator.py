from player import *
from computer import *

cs=0 #computer score    
ps=0 #player score
while cs <5 and ps <5:
    print(f"User: {ps} | Computer: {cs}")
    player_choice=input_checker()
    print(f"You choosed: {player_choice} ")
    computer_choice=random.choice(p)
    print(f"Computer choosed: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a draw!")
    elif (player_choice == "rock" and computer_choice == "scissors"):
        ps += 1
        print("You win this round!")
    elif (player_choice == "scissors" and computer_choice == "paper"):
        ps += 1
        print("You win this round!")
    elif (player_choice == "paper" and computer_choice == "rock"):
        ps += 1
        print("You win this round!")

    else:
        cs += 1
        print("Computer wins this round!")