from typing import Dict


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