
board = ["-", "-", '-', '-', '-', '-', '-', '-', '-']
winner = None
playing = True
var_win = False
tie = False

# the board
def printBoard(board):
    print(f"  {board[0]} | {board[1]} | {board[2]}")
    print("_____________")
    print(f"  {board[3]} | {board[4]} | {board[5]}")
    print("_____________")
    print(f"  {board[6]} | {board[7]} | {board[8]}")
    
index_list = []
# user's input 
def userInput(currentplayer):
    while True:
        
        user = int(input(f"{currentplayer} enter number 1-9:"))
        user -= 1
        if 0 <= user < 10:
            if user in index_list:
                print('This spot is occupied!')
                print('\n')
                continue
            index_list.append(user)
            return user
        else:
            print('Please enter number between 1-9')

   
# Check for win and tie
def checkTie():
    global var_win
    global board
    global tie
    if "-" not in board and var_win == False:
        tie = True  
        print("It is a Tie!")
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[2] != '-':
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[5] != '-':
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[8] != '-':
        winner = board[6]
        return True
    
def checkDiagonal(board):    
    global winner
    if board[0] == board[4] == board[8] and board[8] != '-':
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[6] != '-':
        winner = board[4]
        return True

def checkVertical(board):   
    global winner
    if board[0] == board[3] == board[6] and board[6] != '-':
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[7]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True


#Check for horizontal win
def checkWinner():
    global winner
    if checkVertical(board) or checkDiagonal(board) or checkHorizontal(board):
        var_win = True
        print(f'{winner} won!')
        quit('Thanks for playing :)')

 
# Make 2 player play against each other
# Allow the user to play with the computer(AI)
import random
def computer(board):
    global currentplayer
    while currentplayer == "O":
        comp = random.randint(0, 8)
        if board[comp] == '-':
            board[comp] = player2
            switchplayer()
 
def main():
    player1 = input('Player1 enter your name: ')
    player2 = input('Player2 enter your name: ')
    print('Welcome to the Tic Tac Toe game')
    print(f'{player1} soldiers will be - X')
    print(f'{player2} soldiers will be - O')
    printBoard(board)
    for i in range(9):
       if i % 2 == 0:
           currentplayer = userInput(player1)
           board[currentplayer] = 'X'
           printBoard(board)
       else: 
           currentplayer = userInput(player2)
           board[currentplayer] = 'O'
           printBoard(board)
       print('\n')
       
       checkWinner()
       checkTie()

main()

