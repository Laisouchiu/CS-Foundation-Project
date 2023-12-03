#%%
### DATS-6450 Project Team file

######### Steps ###########
# 1. Set up the board using a list of lists. 
# 2. Create functions that will merge left, right, up, and down. We will create functions to reverse and transpose the list of lists to do this
# 3. Set up the start of the game
# 4. Set up the rounds of the game, where the users will have the option to merge in any one of the 4 directions, and after they move, a new board will display. 
# 5. Set up adding a new value each time after player make a move.
# 6. Set up functions to test if the player has won or lost. 

import numpy as np
import random

board_size = 4 # Because the gameboard is a 4x4 grid

#%%
######### Step 1: Creating a display function ###########

def display(matrix_board):
    # Find and set the space length of the max number in the board as the default length for every unit:
    max = matrix_board[0][0]
    for row in matrix_board: 
        for i in row: 
            if i >max:
                max = i
    space_need = len(str(max))
    
    # Print out the board into a gameboard format
    for row in matrix_board:
        newRow = "|"
        for num in row: 
            if num == 0:
                newRow += " " * space_need + "|"
            else:
                newRow += (" " * (space_need - len(str(num)))) + str(num) + "|"
    
    # Print out the modified matrix
        print(newRow)
    print()

# Test case
test_board = [[0,0,2,2], [2,2,2,0], [4,0,0,4], [0,2,0,0]]
display(test_board)



# %%
######### Step 2: Writing Merging functions ###########
# (Tips: Merging will occur only when the adjacent number of the merging direction is identical)

# Define a reverse function first so that we don't need to left and right merge individually: 
def reverse(row):
    return row[::-1]

# Define a transpose function first so that we can easily define up and down merge later: 
def list_transpose(matrix_board):
    transposed_matrix = np.array(matrix_board).T.tolist()
    return transposed_matrix


# Function to merge only one row left
def one_left(row):
    # Moving every non-zero tiles to left first
    for _ in range(board_size-1):
        for j in range(board_size-1, 0, -1):
            if row[j-1] == 0:
                row[j-1] = row[j]
                row[j] = 0
    # Merging adjacent equal tiles
    for i in range(board_size-1):
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    # Moving non-zero tiles to the left again
    for i in range(board_size-1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    # Finally return the left-merged row
    return row


# Function to merge the whole board matrix left
def left(matrix_board):
    for i in range(board_size): 
        matrix_board[i] = one_left(matrix_board[i])
    return matrix_board

# Function to merge the whole board matrix right
def right(matrix_board):
    for i in range(board_size):
        matrix_board[i] = reverse(matrix_board[i])
        matrix_board[i] = one_left(matrix_board[i])
        matrix_board[i] = reverse(matrix_board[i])
    return matrix_board

# Function to merge the whole board matrix up
def up(matrix_board):
    matrix_board = list_transpose(matrix_board)
    matrix_board = left(matrix_board)
    matrix_board = list_transpose(matrix_board)
    return matrix_board 

# Function to merge the whole board matrix down
def down(matrix_board):
    matrix_board = list_transpose(matrix_board)
    matrix_board = right(matrix_board)
    matrix_board = list_transpose(matrix_board)
    return matrix_board 

# Test case: 
display(test_board)
print('')
display(up(test_board)) # Try either left, or right, or up, or down




# %%
######### Step 3: Set up the start board of the game ###########
## By creating an empty 4x4 gameboard with 2 random tiles valued in either 2 and 4 each

# Create an empty board
start_board = []

# Initially fill lists with zeros and add these lists to the main board list
for _ in range(board_size):
    row = []
    for i in range(board_size):
        row.append(0)
    start_board.append(row)

# Randomly generate a value (either 2 or 4) for a new tile at the begining
# The default probability for the 2048 game is typically such that the value 2 has a higher probability than the value 4.
def two_four_rand():
    if random.randint(1,6) == 4: 
        return 4
    # 1/6 probability to generate a 4, which can change; but remember need to lower than the probability of 2
    else: 
        return 2
    
# Randomly fill two tiles spots in the board with random values to start the game
start_tiles = 2
while start_tiles>0:
    rand_row_index = random.randint(0, board_size-1)
    rand_col_index = random.randint(0, board_size-1)
    if start_board[rand_row_index][rand_col_index] == 0:
        start_board[rand_row_index][rand_col_index] = two_four_rand()
        start_tiles -= 1

# In the standard rules of the 2048 game, 
# a new tile appears after each successful move, 
# and the value of the new tile is typically set to 2. 
# The position of the new tile is random,
# and it can appear in any empty space on the board.

# Test case:
display(start_board)


# %%
######### Step 4-6: Set up the mechanism of the game ###########

# Mechanism for adding a new number
# A new tile appears after each successful move, and the value of the new tile is typically set to 2. 
# The position of the new tile is random, and it can appear in any empty space on the board.

# Officially starting the game
print("Welcome to 2048 Game! You lose, Goodbye!")
print('')
display(start_board)

gameover = False # set as false at initially, because we just started the game

# Set up functions to test if the player has won or lost
def check_win_condition(matrix_board):
    # Check for win condition
    for row in matrix_board:
        if 2048 in row:
            return True
    return False

def check_loss_condition(matrix_board):
    # Check for loss condition
    for row in matrix_board:
        if 0 in row:
            return False
        for i in range(board_size - 1):
            if row[i] == row[i + 1]:
                return False
    return True

# Use while-loop to keep asking the users for new moves as long as the game doesn't over
while not gameover:
    direction = input("What's your move? (left, right, up, down)")

    # if direction.lower() in ['left', 'right', 'up', 'down']:
    #     if direction.lower() == 'left':
    #         start_board = left(start_board)
    #     elif direction.lower() == 'right':
    #         start_board = right(start_board)
    #     elif direction.lower() == 'up':
    #         start_board = up(start_board)
    #     elif direction.lower() == 'down':
    #         start_board = down(start_board)
    
    if direction.lower() in ['a', 'd', 'w', 's']:
        if direction.lower() == 'a':
            start_board = left(start_board)
        elif direction.lower() == 'd':
            start_board = right(start_board)
        elif direction.lower() == 'w':
            start_board = up(start_board)
        elif direction.lower() == 's':
            start_board = down(start_board)

        rand_row_index = random.randint(0, board_size - 1)
        rand_col_index = random.randint(0, board_size - 1)

        while start_board[rand_row_index][rand_col_index] != 0:
            rand_row_index = random.randint(0, board_size - 1)
            rand_col_index = random.randint(0, board_size - 1)

        start_board[rand_row_index][rand_col_index] = two_four_rand()

        display(start_board)

        # Check for win or lose conditions
        if check_win_condition(start_board):
            print("Congratulations! You won!")
            gameover = True
        if check_loss_condition(start_board):
            print("Game over! You lost.")
            gameover = True
            break
    else:
        print("Invalid move. Please enter 'left', 'right', 'up', or 'down'.")

#%%