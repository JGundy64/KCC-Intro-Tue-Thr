from helpers import getNum

def drawBoard(board):
    #TODO - Print the values in the board array parameter. Format them in a tic-tac-toe board (Medium)
    # 1 | 2 | 3
    #-----------
    # 4 | 5 | 6
    #-----------
    # 7 | 8 | 9

def checkWinner(board, player):
    # TODO - Write an if statement to check if there are 3 matching values. Note: there are 8 different combinations to win. For example, if board indexes 0, 1, and 2 are all equal we have a winner. You will need to combine 8 boolean expressions with "or" operators. (Hard)
    
        # TODO - If true, print a message to congratulate the player that won and return True (Easy)
        
    # TODO - Otherwise, return False (Easy)
    

def switchPlayer(player):
    # TODO - Write an if-else statement to change the player from "X" to "O", and vice versa. (Medium)
    
    # TODO - Print a message indicating who the current player is. And return the player variable. (Easy)
    

def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    currentPlayer = "O"
    gameOver = False
    # TODO - Write  while a loop that will run continuosly while the game is not over. Use the gameOver variable. (Easy)
    
        # TODO - Call the drawBoard function, passing the board array to the function. No value will be returned. (Easy)
        
        # TODO - Call the switchPlayer function, passing the currentPlayer variable as the argument. The result returned will be assigned back to the currentPlayer variable. (Medium)
        
        # TODO - Prompt the player for a number between 1 and 9. Give them an infinite amount of attempts. Convert the numerical input to an integer. Assign the player's response to the choice variable. (Medium)
        
        # TODO - Using the choice variable, write a while loop that checks if an "X" or "O" is currently located at the index the player chose. Note: if the user chooses 1, we need to check the value at index 0. If true, prompt the user for another choice using the same logic as the previous TODO (Hard)
        

        # TODO - Assign the currentPlayer variable to location the player chose in the board array. Note: if the user chooses 1, we need to assign the value to index 0. (Medium)
        
        # TODO - Call the checkWinner function. Pass the board array and the currentPlayer to the function. The value returned will be assigned to the gameOver variable. (Medium)
        

main()