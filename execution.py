#%%
# Importing from a module 
import game
import os
import random

#%%
# Create an empty board
board_size = 4 # Because the gameboard is a 4x4 grid
start_board = []

# Initially fill lists with zeros and add these lists to the main board list
for _ in range(board_size):
    row = []
    for i in range(board_size):
        row.append(0)
    start_board.append(row)
    
# Randomly fill two tiles spots in the board with random values to start the game
start_tiles = 2
while start_tiles>0:
    rand_row_index = random.randint(0, board_size-1)
    rand_col_index = random.randint(0, board_size-1)
    if start_board[rand_row_index][rand_col_index] == 0:
        start_board[rand_row_index][rand_col_index] = game.two_four_rand()
        start_tiles -= 1

#%%
# Officially starting the game
# print("Welcome to 2048 Game! You lose, Goodbye!")
print("Welcome to 2048 Game!")
print('')
if os.path.exists("2048_game_state.pickle"):
    resume_choice = input("Do you want to resume the previous game? (y/n): ")
    if resume_choice.lower() in ['y']:
        start_board = game.load_game_state()
        game.delete_saved_game_state()   
    else:
        game.delete_saved_game_state()    
game.display(start_board)

gameover = False # set as false at initially, because we just started the game

# Use while-loop to keep asking the users for new moves as long as the game doesn't over
while not gameover:
    
    direction = input("What's your move? (left, right, up, down)")


    if direction.lower() in ['a', 'd', 'w', 's']:
        if direction.lower() == 'a':
            start_board = game.left(start_board)
        elif direction.lower() == 'd':
            start_board = game.right(start_board)
        elif direction.lower() == 'w':
            start_board = game.up(start_board)
        elif direction.lower() == 's':
            start_board = game.down(start_board)

        rand_row_index = random.randint(0, board_size - 1)
        rand_col_index = random.randint(0, board_size - 1)

        while start_board[rand_row_index][rand_col_index] != 0:
            rand_row_index = random.randint(0, board_size - 1)
            rand_col_index = random.randint(0, board_size - 1)

        start_board[rand_row_index][rand_col_index] = game.two_four_rand()

        game.display(start_board)

        # Check for win or lose conditions
        if game.check_win_condition(start_board):
            print("Congratulations! You won!")
            gameover = True
        if game.check_loss_condition(start_board):
            print("Game over! You lost.")
            gameover = True
            break
 
    elif direction.lower() == 'q':
        save_choice = input("Do you want to save the current game state before quitting? (y/n): ")
        if save_choice.lower() in ['y']:
           game.save_game_state(start_board)
           print("Game saved. Quitting...")
        else:
           print("Game not saved. Quitting...")
           game.delete_saved_game_state()   
        break

    else:
        print("Invalid move. Please enter 'w' for moving up, 'a' for moving left, 's' for moving down, or 'd' for moving right.")
    

# %%
