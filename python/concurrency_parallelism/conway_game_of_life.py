import random
from threading import Lock

# TODO there are some bugs with this code. It corresponds to tips 57, 58, etc.
# I'll have to revisit this later.

class ConwayGameOfLife:
    """Single-threaded Conway game of life."""
    def __init__(self, game_board: list[list[int]]):
        # TODO: consider validating game board.
        self.game_board = game_board
        self.height = len(game_board)
        self.width = len(game_board[0])

    def get(self, x: int, y: int):
        return self.game_board[y % self.height][x % self.width]

    def count_neighbors(self, x: int, y: int, get):
        e = get(x-1, y)
        ne = get(x-1, y+1)
        n = get(x, y+1)
        nw = get(x+1, y+1)
        w = get(x+1, y)
        sw = get(x+1, y-1)
        s = get(x, y-1)
        se = get(x-1, y-1)
        return sum([e, ne, n, nw, w, sw, s, se])
    
    def next_step_cell(self, x: int, y: int, get):
        # TODO: add tests.
        current_cell_value = get(x=x, y=y)
        neighbor_count = self.count_neighbors(x=x, y=y, get=get)
        if current_cell_value == 0 and neighbor_count == 3:
            return 1
        elif current_cell_value == 1 and (neighbor_count == 2 or neighbor_count == 3):
            return 1
        return 0

    def next_step_board(self):
        temp_game_board = self.game_board
        for y in range(self.height):
            for x in range(self.width):
                temp_game_board[y][x] = self.next_step_cell(x=x, y=y, get=self.get)
        self.game_board = temp_game_board
    
    def print_board_state(self):
        print("\nCurrent board state:")
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if self.get(x,y) == 0:
                    row += " - "
                else:
                    row += " * "
            print(row)

class LockedConwayGameOfLife(ConwayGameOfLife):
    """Conway game of life with locks and threads."""
    def __init__(self, game_board: list[list[int]]):
        super().__init__(game_board=game_board)
        self.lock = Lock()
    
    def get(self, x: int, y: int):
        with self.lock:
            super().get(x=x,y=y)

    def count_neighbors(self, x: int, y: int):
        return super().count_neighbors(x, y, self.get)
    
    def next_step_cell(self, x: int, y: int):
        return super().next_step_cell(x, y, self.get)

    def next_step_board(self):
        return super().next_step_board()

def run_game_standard(width: int, height: int):
    game_board = [[random.randint(0,1) for _ in range(width)] for _ in range(height)]
    conway_game = ConwayGameOfLife(game_board=game_board)
    conway_game.print_board_state()
    for _ in range(10):
        conway_game.next_step_board()
        conway_game.print_board_state()

def run_game_locked(width: int, height: int):
    game_board = [[random.randint(0,1) for _ in range(width)] for _ in range(height)]
    locked_conway_game = LockedConwayGameOfLife(game_board=game_board)
    locked_conway_game.print_board_state()
    for _ in range(10):
        locked_conway_game.next_step_board()
        locked_conway_game.print_board_state()