#!/usr/bin/python3

# This script is a Console App for Snakes & Ladder Game
# to Demonstrate the use of SOLID, DRY Principles.

__author__ = 'premkumar30'

from board import Board

GRID_SIZE = 10
BOARD_SIZE = GRID_SIZE * GRID_SIZE
player_position = 00

board = Board(size=GRID_SIZE)

while player_position < BOARD_SIZE:
    pos = int(input("Current Position: "))
    dice = int(input("Dice Outcome: "))

    assert dice <= 6, "Dice result should be within 6"
    assert pos < BOARD_SIZE, \
            f"Position should be within grid size({GRID_SIZE})"

    player_position = board.move_player(dice=dice, pos=pos)
    print('New Position: ', player_position)
