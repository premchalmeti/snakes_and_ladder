#!/usr/bin/python3

# This script is a Console App for Snakes & Ladder Game
# to Demonstrate the use of SOLID, DRY Principles.

__author__ = 'premkumar30'

from typing import Dict


class Player:
    def __init__(self, name: str, grid_size: int) -> None:
        self.name: str = name
        self._current_pos: int = 0
        self.grid_size: int = grid_size

    @property
    def position(self) -> int:
        return self._current_pos

    @position.setter
    def position(self, pos: int) -> None:
        if pos <= (self.grid_size * self.grid_size):
            self._current_pos = pos
        if pos == (self.grid_size * self.grid_size):
            print(f'Player ({self.name}) won!')


class Players:
    def __init__(self, grid_size: int) -> None:
        self.players: Dict[str, Player] = {}

        # add default player
        self.add_player(grid_size)

    def add_player(self, grid_size, p_name: str = 'default',
                   p_id: str = 'A') -> None:
        self.players[p_id] = Player(p_name, grid_size=grid_size)

    def check_if_player_exists(self, p_id: str) -> None:
        assert p_id in self.players, f"{p_id} Player Not Found"

    def get_player(self, p_id: str) -> Player:
        self.check_if_player_exists(p_id)
        return self.players[p_id]


class Snake:
    def __init__(self, head_pos: int, tail_pos: int) -> None:
        self.head_pos: int = head_pos
        self.tail_pos: int = tail_pos


class Snakes:
    def __init__(self) -> None:
        # A map to maintain snake head position with `Snake` object
        self.snakes: Dict[int, Snake] = {}

        # note: Change below lines to take the snakes positions from users
        self.add_snake(36, 19)
        self.add_snake(65, 35)
        self.add_snake(87, 32)
        self.add_snake(97, 21)

    def add_snake(self, head_pos: int, tail_pos: int) -> None:
        self.snakes[head_pos] = Snake(head_pos, tail_pos)

    def is_snake_exists(self, pos: int) -> bool:
        return pos in self.snakes

    def get_tail_pos(self, pos) -> int:
        if not self.is_snake_exists(pos):
            return pos

        snake = self.snakes[pos]

        return snake.tail_pos


class Ladder:
    def __init__(self, ladder_foot: int, ladder_top: int) -> None:
        self.ladder_foot: int = ladder_foot
        self.ladder_top: int = ladder_top


class Ladders:
    def __init__(self) -> None:
        # A map to maintain ladder foot position with `Ladder` object
        self.ladders: Dict[int, Ladder] = {}

        # note: change below lines to take the ladder positions from users
        self.add_ladder(7, 33)
        self.add_ladder(37, 85)
        self.add_ladder(51, 72)
        self.add_ladder(63, 99)

    def add_ladder(self, ladder_foot: int, ladder_top: int) -> None:
        self.ladders[ladder_foot] = Ladder(ladder_foot, ladder_top)

    def is_ladder_exists(self, pos: int) -> bool:
        return pos in self.ladders

    def get_ladder_top(self, pos) -> int:
        if not self.is_ladder_exists(pos):
            return pos

        ladder = self.ladders[pos]

        return ladder.ladder_top


class Board:
    def __init__(self, size: int) -> None:
        """
        Initializes Snakes & Ladder for size X size Board
        """
        self.size: int = size
        self.players: Players = Players(grid_size=size)
        self.snakes: Snakes = Snakes()
        self.ladders: Ladders = Ladders()

    def move_player(self, dice: int, p_id: str = 'A', pos: int = 0) -> int:
        player = self.players.get_player(p_id)
        current_pos = (pos or player.position)
        player.position = current_pos
        new_pos = current_pos + dice

        is_snake = self.snakes.is_snake_exists(new_pos)
        is_ladder = self.ladders.is_ladder_exists(new_pos)

        if is_snake and is_ladder:
            raise Exception(
                f'Ladder and Snake Can Not Exists At Same Position({new_pos})'
            )
        elif is_snake:
            player.position = self.snakes.get_tail_pos(new_pos)
        elif is_ladder:
            player.position = self.ladders.get_ladder_top(new_pos)
        else:
            player.position = new_pos

        return player.position


if __name__ == '__main__':
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
