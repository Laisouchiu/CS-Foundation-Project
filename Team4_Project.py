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
######### Step 1: Creating a display function ###########

def display(matrix):
    # Find and set the space length of the max number in the board as the default length for every unit:
    max = matrix[0][0]
    for row in matrix: 
        for i in row: 
            if i >max:
                max = i
    spaces = len(str(max))
    
    # Print out the board into a gameboard format
    for row in matrix:
        newRow = "|"
        for num in row: 
            if num == 0:
                newRow += " " * spaces + "|"
            else:
                newRow += (" " * (spaces - len(str(num)))) + str(num) + "|"
    
    # Print out the modified matrix
        print(newRow)
    print()

test = [[0,0,0,0], [1,2000,3,4], [7,8,10000,34], [0,4,399,70]]
display(test)


        
# %%
######### Step 2: Creating a merging function ###########