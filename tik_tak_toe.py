# idea
# we need a board to play the game
# a function to display the board
# a function to play the game
# a function to ask what player 1 wants, i.e. 'x' or 'o'
#     a funtion to handle turn
#         a funtion to take input from user
#         a funtion to check if input is valid or not
#         a function to display the updated values on the board after every turn
#         a funtion to switch between players
#         a function to keep taking turns until the game is over
#             a function to check game status
#                 a function to check rows
#                 a function to check columns
#                 a function to check diagonals
#             a function to check if game is tie
#             a function to display winner
# a function to clear board

#=================================Global Variables=============================


#variable to hold bool value on if game is still being played or not
game=True
#variable to hold the player which is the winner
winner=None
#variable to check if the player wants to play again or not
replay=True
#variable to check if the game is a tie or not
tie=False
#variable to take position where the 'x' or 'o' will be placed on the board as an input
position_input=None
#variable to hold the current player
current_player=None


#game board
board=['-', '-', '-',
       '-', '-', '-',
       '-', '-', '-']

#a function to display board
def display_board():
    #an empty line for neater look
    print()
    #printing the elements of the board
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()


#a function to play the game
def play():
    #calling the global variables
    global current_player
    global game
    global tie
    #displaying the board before starting the game
    display_board()
    #checking who wants to go first
    current_player=input("Who wants to go first? x or o:\n")
    #valid choices of pieces to be played
    valid_list=['x', 'X', 'o', 'O']
    #checking if player entered a valid choice
    while current_player not in valid_list:
        print("Invalid choice. Try again.")
        #calling the function to play the game again if player enters an invalid choice
        play()
    while game:
        #calling the function to handle each turn
        handle_turn()
    #calling the function to check if players want to play the game again
    play_again()


#a function to handle turn
def handle_turn():
    #calling the function to take input from the player
    take_input()
    #calling the function to update the game board
    update_board()
    #calling the function to check status of the game
    check_status()
    #calling the function to display the game board
    display_board()
    #calling the function to switch between player 1 and player 2
    switch_players()


#taking input from the player
def take_input():
    #calling the global variables
    global position_input
    #taking input from the current player
    position_input=int(input("Enter a position between 1-9: "))
    #switching to actual position on the board
    #position_input-=1
    #calling the function to check if the position input is valid or not
    check_valid_input()


#a function to check if input is valid or not
def check_valid_input():
    #calling the global variables
    global position_input
    #a list containing all the valid inputs allowed for entering the positions
    valid_input=[1,2,3,4,5,6,7,8,9]
    if position_input not in valid_input:
        print("Invalid choice. Try again.")
        take_input()
    #calling the function to check if the position is already taken or not
    position_already_taken()


#updating game board
def update_board():
    #calling the global variables
    global position_input
    global current_player
    #updating the board with current player's coice
    board[position_input-1]=current_player


#a function to check if the position on the board is already taken or not
def position_already_taken():
    #calling the global variables
    global position_input
    global current_player
    if board[position_input-1]!='-':
        print("This position is already taken. Enter a position that is not taken.")
        take_input()

#a function to switch between players
def switch_players():
    #calling the global variables
    global current_player
    if current_player=='x' or current_player=='X':
        current_player='o'
    else:
        current_player='x'


#a function to check game status
def check_status():
    #calling the global variables
    global tie
    #calling function to check for winner if any
    check_winner()

    if winner!=current_player and tie==False:
        #calling function to check if the game is a tie
        check_tie()


#a function to chech if the game is a tie
def check_tie():
    #calling the global variables
    global tie
    global game
    if '-' not in board:
        tie=True
        game=False
        print("\nThis match is a tie.")


#a function to check winner
def check_winner():
    #calling the global variables
    global game
    #calling the function to check if there is a winner in any of the rows
    check_rows()
    #calling the function to check if there is a winner in any of the columns
    check_columns()
    #calling the function to check if there is a winner in any of the diagonals
    check_diagonals()
    #condition to check if there is a winner or not
    if winner==current_player:
        #setting win status to true
        game=False
        #calling the function to display the winner if there is a winner
        display_winner()
    

#a function to display winner
def display_winner():
    #calling the global variables
    global current_player
    print("\n"+current_player.capitalize()+ " is the winner.")


#a function to check rows
def check_rows():
    #calling the global variables
    global game
    global winner
    row_1=board[0]==board[1]==board[2] !='-'
    row_2=board[3]==board[4]==board[5] !='-'
    row_3=board[6]==board[7]==board[8] !='-'
    if row_1 or row_2 or row_3:
        game=False
        if row_1 or row_2 or row_3:
            winner=current_player


#a function to check columns
def check_columns():
    #calling the global variables
    global game
    global winner
    column_1=board[0]==board[3]==board[6] !='-'
    column_2=board[1]==board[4]==board[7] !='-'
    column_3=board[2]==board[5]==board[8] !='-'
    if column_1 or column_2 or column_3:
        game=False
        if column_1 or column_2 or column_3:
            winner=current_player


#a function to check diagonals
def check_diagonals():
    #calling the global variables
    global game
    global winner
    diagonal_1=board[0]==board[4]==board[8] !='-'
    diagonal_2=board[2]==board[4]==board[6] !='-'
    if diagonal_1 or diagonal_2:
        game=False
        if diagonal_1 or diagonal_2:
            winner=current_player


#a function to clear the board
def clear_board():
    board[0]='-'
    board[1]='-'
    board[2]='-'
    board[3]='-'
    board[4]='-'
    board[5]='-'
    board[6]='-'
    board[7]='-'
    board[8]='-'


#a function to check if players wants to play again or not
def play_again():
    #calling the global variables
    global replay
    #terminal message
    print("Do you want to play again?\n")
    #a variable to hold player's choice if they want to play again or not
    choice=input("Enter 'Y' or 'y' for yes and 'n' or 'N' for no:\n")
    #checking if valid choice entered
    play_choice=['Y', 'y', 'N', 'n']
    while choice not in play_choice:
        print("Invalid choice. Try again.\n")
        #if invalid choice is entered then the same function is called again to take the correct input
        play_again()
    #checking if the players want to play again or not
    if choice=='y' or choice=='Y':
        replay=True
    else:
        replay=False
    #game is being played until the player enteres 'n' on 'N'
    while replay:
        #setting the choice variable as none to remove previous entries
        choice=None
        #calling the function to clear the board to start a new game
        clear_board()
        #calling the function to reset the global values before starting a new game
        reset()
        #function is called to play the game again
        play()


#a function to reset the values for a new game
def reset():
    #calling the global variables
    global game
    global winner
    global replay
    global tie
    global position_input
    global current_player

    game=True
    winner=None
    replay=False
    tie=False
    position_input=None
    current_player=None


#calling the function to play the game
play()