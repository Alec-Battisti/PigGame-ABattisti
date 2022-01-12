'''Player object file'''
from Msg import message
import math


class Player:
    def __init__(self, name):
        self.Name = name
        self.Score = 0

    def getRollDecision(self, turnScore, turnRolls, players):
        answer = ''
        while answer != 'y' and answer != 'n':
            message(self.Name + ": Would you like to roll? (y/n)")
            answer = input()
        return True if answer == 'y' else False

    def award(self, points):
        self.Score += points


class Computer:
    def __init__(self):
        self.Name = "PIGNET"
        self.Score = 0
        self.totalTurns = 1

    def getRollDecision(self, turnScore, turnRolls, players):
        opposingScore = players[0].Score if players[0].Name != "PIGNET" else players[1].Score
        if turnScore < (opposingScore/self.totalTurns) and (self.Score + turnScore < 100):
            self.totalTurns += 1
            return True
        else:
            self.totalTurns += 1
            return False

    def award(self, points):
        self.Score += points
