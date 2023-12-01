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



#%%
######### Write your code below ###########

def display(board):
    for row in board:
        newRow = "|"
        for num in row: 
            if num == 0:
                newRow += " |"
            else:
                newRow += str(num) + "|"
        print(newRow)
    print()

test = [[0,0,0,0], [1,2,3,4]]
display(test)
        
# %%
