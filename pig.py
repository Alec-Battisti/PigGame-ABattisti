#!/usr/bin/env python3
# Alec Battisti
# CPSC 386-01
# 10/17/2021
# alec.battisti@csu.fullerton.edu
# Pig Game assignment
'''main function'''
from pig_game import PigGame
from Msg import message

'''specify number of players and start game'''


def main():
    numPlayers = -1
    while True:
        message("How many players?")
        numPlayers = input()
        if int(numPlayers) > 0 and int(numPlayers) <= 4:
            break
        else:
            message("Invalid player count")
    game = PigGame(numPlayers)
    game.play()


main()
