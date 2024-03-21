from snakesAndLadderss.models.board import Board
from snakesAndLadderss.services.dice_service import DiceService

class SnakeAndLadderService:
    def __init__(self, size=100):
        self.board = Board(size)
        #default size is 100

    def setPlayers(self, players):
        self.playerQueue = []
        self.initialNumberOfPlayers = len(players)
        playerPostions = {}
        for player in players:
            #fifo queue for players
            self.playerQueue.append(player)
            #initially all players at 0
            playerPostions[player.getId()] = 0
        self.board.playersCurrentPostions = playerPostions
    def setSnakes(self, snakes):
        self.board.snakeList = snakes
    def setLadders(self, ladders):
        self.board.ladderList = ladders
    def getTotalValueAfterDiceRolls(self):
        return DiceService.roll()
    def getNewPositionAfterDiceRolls(self, player, position):
        print("Processing Position"+ str(position)+ " for "+ player.getName())
        while True:
            for ladder in self.board.ladderList:
                if ladder.getSource() == position:
                    print(player.getName() + "Ladder at "+ str(position)+ " Moved to postion " + str(ladder.getDestination()))
                    position = ladder.getDestination()
                    continue
            for snake in self.board.snakeList:
                if snake.getSource() == position:
                    print(player.getName() + "Snake at "+ str(position)+ " Moved to postion " + str(snake.getDestination()))
                    position = snake.getDestination()
                    continue
            break
        return position
    def movePlayer(self, player, diceValue):
        oldPosition = self.board.playersCurrentPositions[player.getId()]
        newPosition = oldPosition + diceValue
        boardSize = self.board.getSize()
        if newPosition > boardSize:
            newPosition = oldPosition
        else:
            newPosition = self.getNewPositionAfterDiceRolls(player, newPosition)
        self.board.playersCurrentPositions[player.getId()] = newPosition

    def hasPlayerWon(self, player):
        return self.board.getPlayersCurrentPositions().get(player.getId()) == self.board.getSize()
    
    def isGameCompleted(self):
        return self.initialNumberOfPlayers > len(self.playerQueue)
    def startGame(self):
        while(self.isGameCompleted() == False):
            diceValue = self.getTotalValueAfterDiceRolls()
            player =self.playerQueue.pop(0)
            self.movePlayer(player, diceValue)
            if self.hasPlayerWon(player) == True:
                print(player.getName() + " has won the game")
                self.board.getPlayersCurrentPositions().pop(player.getId())
                break
            else:
                self.playerQueue.append(player)

snakes = SnakeAndLadderService()