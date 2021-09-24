class Enemy:
    def __init__(self, initialRow, initialColumn):
        self.rowPosition = initialRow
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
