import random
import sys

class Game(object):  
  def __init__(self, prisoners, log):
    self.log = log
    self.binaryIndicator = False
    self.prisonerList = [Prisoner() for i in range(prisoners)]
    self.visits = 0
    random.choice(self.prisonerList).isKey = True
    
  def runGame(self):
    while True:
      tempPrisoner = random.choice(self.prisonerList)
      if self.log:
        print()
        print(self.prisonerList.index(tempPrisoner))
        print(self.binaryIndicator)
        tempPrisoner.printMe()
      self.binaryIndicator = tempPrisoner.makeChoice(self.binaryIndicator)
      if self.log:
        print(self.binaryIndicator)
        tempPrisoner.printMe()
      self.visits +=1
      if tempPrisoner.countOfPrisoners == (len(self.prisonerList)-1):  #I would prefer this decision be made by the Prisoner class
        if self.log:
          print("Game Over")
          print("Visits: "+str(self.visits)) #
        break
      
class Prisoner(Game):
  def __init__(self):
    self.isKey = False
    self.hasFlippedBit = False
    self.countOfPrisoners = 0
    self.gameOver = False #currently not in use
  
  def printMe(self):
    print(self.isKey, self.hasFlippedBit, self.countOfPrisoners,self.gameOver)
  
  def makeChoice(self,binaryIndicator):
    if self.isKey:
      if binaryIndicator:
        self.countOfPrisoners+=1
        #if self.countOfPrisoners == len(self.prisonerList):  #The decision on whether it's done should be made by Prisoners and not the Game
        #  self.gameOver = True
        return False
      else:
        return binaryIndicator
      
    else:
      if self.hasFlippedBit:
        return binaryIndicator
      else:
        if binaryIndicator:
          return binaryIndicator
        else:
          self.hasFlippedBit = True
          return True

if __name__ == '__main__':
  prisoners, logging = int(sys.argv[1]), bool(int(sys.argv[2])) #prisoners = int(input("How many prisoners?\n"))
  myGame = Game(prisoners, logging)
  myGame.runGame()