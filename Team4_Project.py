#%%
### DATS-6450 Project Team file


#%%
######### Steps ###########
# 1. Set up the board using a list of lists. 
# 2. Create functions that will merge left, right, up, and down. We will create functions to reverse and transpose the list of lists to do this
# 3. Set up the start of the game, by creating an empty gameboard with 2 random unit (value in either 2 and 4)
# 4. Set up the rounds of the game, where the users will have the option to merge in any one of the 4 directions, and after they move, a new board will display. 
# 5. Set up adding a new value each time after player make a move.
# 6. Set up functions to test if the player has won or lost. 

board_size = 4

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

test_board = [[0,0,2,2], [2,2,2,0], [4,0,0,4], [0,2,0,0]]
display(test_board)

        
# %%
######### Step 2: Creating a merging functions ###########
# Tips: Merging will occur only when the adjacent number of the merging direction is identical

# Function to merge only one row left: 
def one_left(row):
    
    for i in range(board_size-1):
        for j in range(board_size-1, 0 ,-1):
            if row[j-1] == 0:
                row[j-1] = row[j]
                row[j] = 0
    
    for i in range(board_size-1):
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    
    for i in range(board_size-1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    
    # Finally return the left-merged row
    return row

test_row1 = [1, 2000, 3, 4]
test_row2 = [2, 2, 0, 4]

result1 = one_left(test_row1)
result2 = one_left(test_row2)
print(result1)
print(result2)


# Function to merge the whole board matrix left
def left(matrix_board):
    for i in range(board_size): 
        matrix_board[i] = one_left(matrix_board[i])
    
    return matrix_board


display(left(test_board))



# %%
