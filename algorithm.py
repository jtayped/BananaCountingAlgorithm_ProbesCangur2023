class Exercise28ProbesCangur:
    def __init__(self, matrix, word) -> None:
        self.matrix, self.word = matrix, word
        self.combinations = 0
        self.initPosition = [0, 0]
    
    def calculate(self):
        for move in self.getMoves(self.matrix, self.initPosition):
            firstLetters = self.getLetterAtIndex(self.matrix, self.initPosition)+self.getLetterAtIndex(self.matrix, move)
            self.combinations += self.calculateWord(self.matrix, move, firstLetters, self.word, len(self.word)-2)
        
        return self.combinations

    def getLetterAtIndex(self, matrix, position):
        return matrix[position[0]][position[1]]

    def getMoves(self, matrix, position):
        moves = []

        for colIndex,col in enumerate(matrix):
            for rowIndex,row in enumerate(col):
                if self.validMove(matrix, position, (colIndex, rowIndex)):
                    moves.append([colIndex, rowIndex])

        return moves

    def validMove(self, matrix, position, move):
        colPos, rowPos = position
        colMove, rowMove = move
        
        # Out of bounds
        if colMove > len(matrix)-1 or colMove < 0 or rowMove > len(matrix[colMove])-1 or rowMove < 0:
            return False

        # Only one move in all directions and no diagonal movement
        colDiff = abs(colPos - colMove)
        rowDiff = abs(rowPos - rowMove)
        if colDiff > 1 or rowDiff > 1 or (colDiff == 0 and rowDiff == 0) or (colDiff == 1 and rowDiff == 1):
            return False
        
        return True

    def wordCorrect(self, word, correctWord):
        if word in correctWord:
            return True
        return False

    def calculateWord(self, matrix, position, word, correctWord, depth):
        if depth == 0 or not self.wordCorrect(word, correctWord):
            if word == correctWord:
                return 1
            else:
                return 0
        
        count = 0
        for move in self.getMoves(matrix, position):
            new_word = word + self.getLetterAtIndex(matrix, move)
            count += self.calculateWord(matrix, move, new_word, correctWord, depth-1)
            
        return count