# CS-Foundation-Project
This is a group project of Computer Science Foundation class in Fall 2023. We decided to design an Python package about 2048 game. Now, let us walk you through this repo.  

There are some files you may concern in this repo:  
**Game.py**: This is an package file containing all defined functions about 2048 games. We used this package as a dependency in this project.  
**Execution.py**: Players can initiate 2048 game from this file.  
**Team4_project.py**: This file contains almost all of the codes regarding of the 2048 game. We started coding from this file.   
**Team4_Project_save.py**: We added more functions to this project, like how to store state of games, how to resume it.  
**Reference_2048_Game.py**: This file is created using the pygame package to develop the 2048 game. It includes the design of the user interface and utilizes the arrow keys on the keyboard for navigation. We consider this file as a reference project for creating the final project.

## What's 2048 game? 
The 2048 game is a puzzle game where the goal is to combine numbered tiles to reach the tile with the number 2048. The **standard rules** for the 2048 game are as follows:

**Game Board**: The game is played on a 4x4 grid.  
**Tiles**: The game starts with two tiles, each having a value of either 2 or 4, placed randomly on the grid.  
**Tile Movement**: The player can move the tiles in four directions: up, down, left, and right. All the tiles on the board will move in the chosen direction as far as possible, until they either hit the edge of the grid or another tile.  
**Merging**: When two tiles with the same number collide as a result of a move, they merge into a tile with a value equal to the sum of their values. For example, if two tiles with a value of 2 collide, they merge into a single tile with a value of 4.  
**Scoring**: The player's score is the sum of all merged tile values. The goal is to achieve the tile with the value 2048.  
**Game Over**: The game is over when there are no valid moves left (i.e., when the grid is full, and no adjacent tiles can be merged). The player's final score is recorded.  

## How did we make 2048 Game in Python? 
- Set up a Display function 
- Set up Merging functions 
- Start Board Setup
- Game Mechanisms Setup  
  - Win/Loss Conditions
- Game Loop

## How to play? 
### Play from initial game state
1. Open and run game.py
2. Open and run execution.py
3. Enter 'w' for Up, 'a' for Left, 's' for Down, 'd' for Right
4. Enter ‘q’ to quit the game
    - Enter ‘y’ if you want to save the current game state before quitting
    - Enter ‘n’ if you don’t want to save

### Resume the game
1. Open and run game.py
2. Open and run execution.py
    - Enter ‘y’ to resume the previous game
    - Enter ‘n’ if you don’t  want to resume the previous game
