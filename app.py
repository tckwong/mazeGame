import gameboard
import player


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

while True:
    board.printBoard(played.rowPosition, played.columnPosition)
    selection = input("Make a move: ")
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

    # Move the player through the board
    # Check if the player has won, if so print a message and break the loop!
    playerWon = board.checkWin(played.rowPosition, played.columnPosition)
    if (playerWon == True):
        print("\U0001f600 You win!!! \U0001f600")
        break
    else:
        continue