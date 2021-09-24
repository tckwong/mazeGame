class GameBoard:
    def __init__(self, coin=False):
        self.playerEmoji = "\U0001f476 "
        self.coinEmoji = "\U0001f4B0 "
        self.enemyEmoji = "\U0001f47B "
        self.winningRow = 0
        self.winningColumn = 2
        self.coinRowLocation = 2
        self.coinColumnLocation = 4
        self.coinTaken = coin
        self.board = [
            [" * ", " * ", "   ", " * ", " * ", " * ", " * ", " * ", " * ", " * "],
            [" * ", "   ", "   ", "   ", " * ", " * ", " * ", " * ", " * ", " * "],
            [" * ", "   ", " * ", " * ", "   ", " * ", " * ", " * ", " * ", " * "],
            [" * ", "   ", "   ", "   ", "   ", " * ", " * ", " * ", " * ", " * "],
            [" * ", " * ", " * ", "   ", " * ", " * ", " * ", " * ", " * ", " * "],
            [" * ", " * ", "   ", "   ", " * ", " * ", "   ", "   ", " * ", " * "],
            [" * ", " * ", "   ", " * ", " * ", " * ", " * ", "   ", " * ", " * "],
            [" * ", " * ", "   ", " * ", " * ", " * ", " * ", "   ", " * ", " * "],
            [" * ", " * ", "   ", "   ", "   ", "   ", "   ", "   ", " * ", " * "],
            [" * ", " * ", "   ", " * ", " * ", " * ", " * ", " * ", " * ", " * "],
            [" * ", " * ", "   ", " * ", " * ", " * ", "   ", " * ", " * ", " * "],
            [" * ", " * ", "   ", "   ", "   ", "   ", "   ", " * ", " * ", " * "],
            [" * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn, badGuyRow, badguyColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(self.playerEmoji, end="")
                elif (i == self.coinRowLocation and j == self.coinColumnLocation and self.coinTaken == False):
                    print(self.coinEmoji, end="")
                elif i == badGuyRow and j == badguyColumn:
                    print(self.enemyEmoji, end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    #Checks to see if wall or enemy is blocking path. Prevents movement
    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            return False
        return True
    
    #Check coin and sets value to true if player lands on the same space as coin
    def checkCoin(self, playerRow, playerColumn):
        if (playerRow == self.coinRowLocation and playerColumn == self.coinColumnLocation):
            print("Found some money!")
            self.coinTaken = True
            return True
        return False
    
    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if (playerRow == self.winningRow and playerColumn == self.winningColumn):
            return True
        else:
            return False
    
