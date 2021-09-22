class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # def moveUp(self):
    def moveUp(self):
        self.rowPosition -= 1
    # def moveDown(self):
    def moveDown(self):
        self.rowPosition += 1
    # def moveLeft(self):
    def moveLeft(self):
        self.columnPosition -= 1
    # def moveRight(self):
    def moveRight(self):
        self.columnPosition += 1
