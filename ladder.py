from typing import Dict


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
