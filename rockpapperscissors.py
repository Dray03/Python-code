# Import random to activate the random built-in function.
import random

# Create a tuple variable containing the option to choose from.
tools = ("rock", "paper", "scissors")

playing = True

# Keep record of the player's scores and the computer's scores.
p_scores = 0
comp_scores = 0

while playing:
    
    # Print the tools
    print(tools)
    
    # Prompt the player to select a tool from the above options.
    player = input("Select a tool: ").lower()
    print(f'Player chose {player:} and computer chose {comp:}')
    
    
    # Make the computer select tools by itself(randomly).
    # Use random.choice to select a tool from the tuple.
    comp = random.choice(tools)

    # Compare the player's tool and the computer's tool and decide who wins and who loses.
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
    print(f'You have {p_scores} point and the computer has {comp_scores} point')    

    # Give the player the option to play again.
    # Player must press "p" to play again
    play_again = input("press 'p' to play again: ").lower()
    if play_again != "p":
        break

    
   
    
