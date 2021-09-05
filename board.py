from player import Players
from snake import Snakes
from ladder import Ladders


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
