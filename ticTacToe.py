#!/usr/bin/env python3

class Board:
    boxNumbers = {1: (0,0), 2: (0, 1), 3: (0, 2),
              4: (1,0), 5: (1, 1), 6: (1, 2),
              7: (2,0), 8: (2, 1), 9: (2, 2)}

    def __init__(self, n):
        self.rows = n
        self.cols = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def __str__(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                val = " "
                if self.board[i][j] != 0: 
                    val = self.board[i][j]
                if j < (len(self.board[0]) - 1):
                    print(val,"|" ,end =" ")
                else:
                    print(val)
            if i == 2: continue
            print("----------")
        return ''       

    def printHintBoard(self):
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                count += 1
                if j < (len(self.board[0]) - 1):
                    print(count,"|" ,end =" ")
                else:
                    print(count)
            if i == 2: continue
            print("----------")
    
    # is empty
    def isEmpty(self, i, j):
      if self.isValidIndex(i, j):
        return self.board[i][j] == 0
      else:
        print("invalid index, valid inputs: 0 <= row < 3 and 0 <= col < 3")
        return False 
    
    def isValidIndex(self, i, j):
      return 0 <= i < self.rows and 0 <= j < self.cols

    # add move 
    def addMoveIJ(self, i, j, val):
        if self.isEmpty(i, j):
          self.board[i][j] = val
          return True
        return False

    def addMove(self, boxNum, val):
      if boxNum < 1 or boxNum > 9: return False
      i, j = self.boxNumbers[boxNum]
      return self.addMoveIJ(i, j, val)

    def getVal(self, i, j):
      if self.isValidIndex(i, j):
        return self.board[i][j]
      else:
        print("Invalid box number")
        return
    '''
    X |   | O
    ---------
    X | O |  
    ---------
      | X | X
    '''
    
    
class Player:
    def __init__(self, name, val):
        self.name = name
        self.val = val
    
    


def isWon(b, rows, cols, val):
  # check rows
  for i in range(rows):
    currSum = 0
    for j in range(cols):
      bVal = b.getVal(i, j)
      if type(bVal) == int:
         continue
      elif bVal == val:
        currSum += 1
        if currSum == 3: return True
        
  # check cols
  for j in range(cols):
    currSum = 0
    for i in range(rows):
      bVal = b.getVal(i, j)
      if type(bVal) == int:
         continue
      elif bVal == val:
        currSum += 1
        if currSum == 3: return True

  # check diagonal
  currSum = 0
  for i in range(cols):
      bVal = b.getVal(i, i)
      if type(bVal) == int:
         continue
      elif bVal == val:
        currSum += 1
        if currSum == 3: return True

  # check anti diagonal
  currSum = 0
  for i in reversed(range(rows)):
      bVal = b.getVal(i, rows - 1 - i)
      if type(bVal) == int:
         continue
      elif bVal == val:
        currSum += 1
        if currSum == 3: return True
  return False

# MARK
# Start of Game Code
# ===================
p1 = Player("Pam","X")
p2 = Player("Jim","O")

b = Board(3)

isPlayer1Turn = True
currPlayer = p1
print("Each box in the board is represented by the numbers below")
b.printHintBoard()
print("Your board is empty at the moment: ")
print(b)

for i in range(9):
  if isPlayer1Turn:
    currPlayer = p1
  else:
    currPlayer = p2

  print(f"Hi {currPlayer.name}")

  boxNum = input("Enter the box number you want to fill: ")
  if not boxNum.isdigit():
    print("Invalid Box Number: Make sure you entered a number 1-9 and the box is empty!")
    i = i - 1
    isPlayer1Turn = not isPlayer1Turn

  # add the move if possible
  else:
    addedMove = b.addMove(int(boxNum), currPlayer.val)
    if not addedMove: 
      print("Invalid Box Number: Make sure you entered a number 1-9 and the box is empty!")
      i = i - 1
      isPlayer1Turn = not isPlayer1Turn
    
    print(b)
    if isWon(b, 3, 3, currPlayer.val):
        print(f"{currPlayer.name} won!")
        break

  isPlayer1Turn = not isPlayer1Turn