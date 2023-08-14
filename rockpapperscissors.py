
import random

tools = ("rock", "paper", "scissors")

playing = True
p_scores = 0
comp_scores = 0

while playing:
    comp = random.choice(tools)
    
    print(tools)
    player = input("Select a tool: ").lower()
    print(f'Player chose {player:} and computer chose {comp:}')

    if player == comp:
        print("Tie")
    elif player == "rock" and comp == "scissors":
        print("You won :)")
        p_scores += 1
    elif player == "scissors" and comp == "paper":
        print("You won :)")
        p_scores += 1
    elif player == "rock" and comp == "scissors":
        print("You won :)")
        p_scores += 1
    elif player == "paper" and comp == "rock":
        print("You won :)")
        p_scores += 1
    else:
        print("You lose :(")
        comp_scores += 1
    print(f'You have {p_scores:} point and the computer has {comp_scores:}')    
    
    play_again = input("press 'p' to play again: ").lower()
    if play_again != "p":
        break

    
   
    
