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