class Board:
    def __init__(self,size):
        self.size = size
        self.snakeList = []
        self.ladderList = []
        # assuming this is a multi-player game played in First in First out mode
        self.playersCurrentPostion = {}

    def setSize(self,size):
        self.size = size
    def getSize(self):
        return self.size
    def setSnakeList(self,snakeList):
        self.snakeList = snakeList
    def getSnakeList(self):
        return self.snakeList
    def setLadderList(self, ladderList):
        self.ladderList = ladderList
    def getLadderList(self):
        return self.ladderList
    def setPlayersCurrentPostion(self, playersCurrentPostion):
        self.playersCurrentPostion = playersCurrentPostion
    def getPlayersCurrentPostion(self):
        return self.playersCurrentPostion