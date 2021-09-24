import gameboard
import player
import enemy
import random

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")

print("Try to get to the end! Good Luck!")
print("-----------------------------")

# Create a new GameBoard called board
# Create a new Player called played starting at position 3,2
board = gameboard.GameBoard()
played = player.Player(3,2)
enemyed = enemy.Enemy(7,2)
enemyChoices = ["up", "left", "down", "right"]
coinsCollected = 0
while True:
    board.printBoard(played.rowPosition, played.columnPosition, enemyed.rowPosition, enemyed.columnPosition)
    selection = input("Make a move: ")
    #Enemy move randomly generated based on list 'enemyChoices'
    enemyChoose = random.choice(enemyChoices)
    coinsCollected = coinsCollected
    print("$ collected: ", coinsCollected)
    
    if (selection == "a"):
        if (board.checkMove(played.rowPosition, played.columnPosition-1)):
            played.moveLeft()
    elif (selection == "d"):
        if (board.checkMove(played.rowPosition, played.columnPosition+1)):
            played.moveRight()
    elif (selection == "w"):
        if (board.checkMove(played.rowPosition-1, played.columnPosition)):
            played.moveUp()
    elif (selection == "s"):
        if (board.checkMove(played.rowPosition+1, played.columnPosition)):
            played.moveDown()

    #Check for coin taken
    checkforMoney = board.checkCoin(played.rowPosition, played.columnPosition)
    
    if checkforMoney:
            coinsCollected += 100
    
    #Check for Loss (This conditional statement is used here to catches the scenario where player moves into enemy space,
    # and the enemy moves into player space at the same time.)
    if(played.rowPosition == enemyed.rowPosition and played.columnPosition == enemyed.columnPosition):
        print("You lose!!")
        break

    #Enemy Moves
    if (enemyChoose == "left"):
        if (board.checkMove(enemyed.rowPosition, enemyed.columnPosition-1)):
            enemyed.moveLeft()
    elif (enemyChoose == "right"):
        if (board.checkMove(enemyed.rowPosition, enemyed.columnPosition+1)):
            enemyed.moveRight()
    elif (enemyChoose == "up"):
        if (board.checkMove(enemyed.rowPosition-1, enemyed.columnPosition)):
            enemyed.moveUp()
    elif (enemyChoose == "down"):
        if (board.checkMove(enemyed.rowPosition+1, enemyed.columnPosition)):
            enemyed.moveDown()
    
    #Check for Loss
    if(played.rowPosition == enemyed.rowPosition and played.columnPosition == enemyed.columnPosition):
        print("You lose!!")
        break
    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
    playerWon = board.checkWin(played.rowPosition, played.columnPosition)
    if (playerWon):
        print("\U0001f600 You win!!! \U0001f600") #\U0001f4B0
        break
    else:
        continue