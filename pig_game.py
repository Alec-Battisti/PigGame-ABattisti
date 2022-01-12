'''This is the pig game object'''
from player import Player, Computer
from die import Die
import random
from Msg import message


class PigGame:
    turnScore = 0
    turnRolls = 0
    lastRoll = 0

    def __init__(self, numPlayers=1, playUntil=100):
        self.numPlayers = int(numPlayers)
        self.Goal = playUntil
        self.Die = Die()
        self.Players = self.getPlayerNames()

    def getPlayerNames(self):
        playerList = list()
        for x in range(self.numPlayers):
            message("Player" + str(x) + " name?")
            name = input()
            playerList.append(Player(name))
        if self.numPlayers == 1:
            playerList.append(Computer())
        random.shuffle(playerList)
        return playerList

    def displayScore(self):
        for x in self.Players:
            message(x.Name + ": " + str(x.Score))

    def winner(self):
        for x in self.Players:
            if x.Score >= self.Goal:
                return x
        return None

    def play(self):
        turnIterator = iter(self.Players)
        while not self.winner():
            currentPlayer = None
            self.displayScore()
            try:
                currentPlayer = next(turnIterator)
            except StopIteration:
                turnIterator = iter(self.Players)
                currentPlayer = next(turnIterator)
            message("It is " + currentPlayer.Name + "'s turn!")
            result = self.Die.Roll()
            self.lastRoll = result
            self.turnScore += result
            self.turnRolls += 1
            message("You rolled a " + str(result))
            while self.lastRoll != 1:
                message("This turn: " + str(self.turnScore))
                message("Rolls: " + str(self.turnRolls))
                if currentPlayer.getRollDecision(self.turnScore,
                                                 self.turnRolls,
                                                 self.Players):
                    result = self.Die.Roll()
                    self.lastRoll = result
                    self.turnScore += result
                    self.turnRolls += 1
                    message("You rolled a " + str(result))

                else:
                    currentPlayer.award(self.turnScore)
                    break
            self.turnScore = 0
            self.turnRolls = 0
            self.lastRoll = 0

        winner = self.winner()
        if winner:
            message(winner.Name + " wins the game!")
