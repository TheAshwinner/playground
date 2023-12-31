# TODO there are some bugs with this code. It corresponds to tips 57, 58, etc.
# I'll have to revisit this later.

# Current learnings:
# 1. pass functions instead of classes as arguments to simplify interfaces (item 38)
# 2. Locks should be added on the lowest possible granularity. Adding multiple levels
# of locks can cause deadlocks (or at least some other issues).
# 3. Avoid using threads for fanout: at least in this case, it seems to
# increase the time the program takes to run by an order of magnitude.
from concurrent.futures import ThreadPoolExecutor
from threading import Lock, Thread
import time
import asyncio

ALIVE = "*"
DEAD = "-"
STEP_COUNT = 10


class Grid:
    """Grid representing Conway's game of life,"""

    def __init__(self, width: int, height: int):
        # TODO: consider validating game board.
        self.height = height
        self.width = width
        self.game_board = [
            [DEAD for _ in range(self.width)] for _ in range(self.height)
        ]

    def get(self, x: int, y: int):
        return self.game_board[y % self.height][x % self.width]

    def set(self, x: int, y: int, val):
        self.game_board[y % self.height][x % self.width] = val

    def __str__(self):
        grid_str = "\nCurrent board state:"
        for y in range(self.height):
            row = ""
            for x in range(self.width):
                if self.get(x, y) == DEAD:
                    row += "-"
                elif self.get(x, y) == ALIVE:
                    row += "*"
                else:
                    raise ValueError("Cells should only be DEAD or ALIVE.")
            grid_str += "\n" + row
        return grid_str


class LockedGrid(Grid):
    """Grid with locks representing Conway's game of life,"""

    def __init__(self, width: int, height: int):
        super().__init__(width=width, height=height)
        self.lock = Lock()

    def get(self, x: int, y: int):
        with self.lock:
            return super().get(x=x, y=y)

    def set(self, x: int, y: int, val):
        with self.lock:
            super().set(x=x, y=y, val=val)


def count_neighbors(x: int, y: int, get):
    """Count all the alive neighbors of a given cell.

    Note that this uses item 38: accept functions instead
    of classes for simple interfaces.
    """
    e = get(x - 1, y)
    ne = get(x - 1, y + 1)
    n = get(x, y + 1)
    nw = get(x + 1, y + 1)
    w = get(x + 1, y)
    sw = get(x + 1, y - 1)
    s = get(x, y - 1)
    se = get(x - 1, y - 1)
    neighbor_states = [e, ne, n, nw, w, sw, s, se]
    neighbor_count = 0
    for state in neighbor_states:
        if state == ALIVE:
            neighbor_count += 1
    return neighbor_count


def game_logic(state, alive_neighbor_count: int):
    if state == DEAD and alive_neighbor_count == 3:
        return ALIVE  # Regenerate
    elif state == ALIVE:
        if alive_neighbor_count > 3:
            return DEAD  # Die: too many.
        elif alive_neighbor_count < 2:
            return DEAD  # Die: too few.
    return state


async def game_logic_coroutine(state, alive_neighbor_count: int):
    if state == DEAD and alive_neighbor_count == 3:
        return ALIVE  # Regenerate
    elif state == ALIVE:
        if alive_neighbor_count > 3:
            return DEAD  # Die: too many.
        elif alive_neighbor_count < 2:
            return DEAD  # Die: too few.
    return state


def step_cell(x: int, y: int, get, set):
    state = get(x, y)
    neighbors = count_neighbors(x=x, y=y, get=get)
    next_state = game_logic(state=state, alive_neighbor_count=neighbors)
    set(x, y, next_state)


async def step_cell_coroutine(x: int, y: int, get, set):
    state = get(x, y)
    neighbors = count_neighbors(x=x, y=y, get=get)
    next_state = await game_logic_coroutine(state=state, alive_neighbor_count=neighbors)
    set(x, y, next_state)


def simulate(grid: Grid):
    next_grid = Grid(height=grid.height, width=grid.width)
    for y in range(grid.height):
        for x in range(grid.width):
            step_cell(x=x, y=y, get=grid.get, set=next_grid.set)
    print(next_grid)
    return next_grid


def simulate_threaded(grid: Grid):
    next_grid = LockedGrid(height=grid.height, width=grid.width)
    threads: list[Thread] = []
    for y in range(grid.height):
        for x in range(grid.width):
            args = (x, y, grid.get, next_grid.set)
            thread = Thread(target=step_cell, args=args)
            thread.start()  # Fan out
            threads.append(thread)
    for thread in threads:
        thread.join()
    print(next_grid)
    return next_grid


def simulate_pool(pool: ThreadPoolExecutor, grid: Grid) -> Grid:
    next_grid = LockedGrid(height=grid.height, width=grid.width)
    futures: list[ThreadPoolExecutor] = []
    for y in range(grid.height):
        for x in range(grid.width):
            args = (x, y, grid.get, next_grid.set)
            future = pool.submit(step_cell, *args)
            futures.append(future)
    for future in futures:
        future.result()
    print(next_grid)
    return next_grid


async def simulate_coroutine(grid: Grid):
    next_grid = Grid(height=grid.height, width=grid.width)
    tasks = []
    for y in range(grid.height):
        for x in range(grid.width):
            task = step_cell_coroutine(x=x, y=y, get=grid.get, set=next_grid.set)
            tasks.append(task)

    await asyncio.gather(*tasks)
    print(next_grid)
    return next_grid


def generate_grid1(width: int, height: int, grid: Grid) -> Grid:
    """Generate grid.
    Initial grid:
    *---
    --*-
    --**
    *---
    """
    grid.set(x=0, y=0, val=ALIVE)
    grid.set(x=2, y=1, val=ALIVE)
    grid.set(x=2, y=2, val=ALIVE)
    grid.set(x=3, y=2, val=ALIVE)
    grid.set(x=0, y=3, val=ALIVE)
    return grid


def run_game_standard(width: int, height: int):
    """Run Conway Game of Life simulator."""
    start_time = time.time()
    grid = Grid(width=width, height=height)
    grid = generate_grid1(width=width, height=height, grid=grid)
    print(grid.__str__())
    for _ in range(STEP_COUNT):
        grid = simulate(grid=grid)
    end_time = time.time()
    print(f"Total time taken: {end_time-start_time:.3} seconds.")


def run_game_locked(width: int, height: int):
    """Run Conway Game of Life simulator with threads.

    When benchmarking this function, it seems to take about an order
    of magnitude longer to run than `run_game_standard()`. This is
    likely due to the overhead of creating threads.
    """
    start_time = time.time()
    grid = LockedGrid(width=width, height=height)
    grid = generate_grid1(width=width, height=height, grid=grid)
    print(grid.__str__())
    for _ in range(STEP_COUNT):
        grid = simulate_threaded(grid=grid)
    end_time = time.time()
    print(f"Total time taken: {end_time-start_time:.3} seconds.")


def run_game_pooled(width: int, height: int):
    """Run Conway Game of Life simulator with ThreadPoolExecutor.

    This corresponds to tip 59 in Effective Python. It allows easier
    refactoring than queues, and threads can be allocated in advance
    so we don't need to pay the overhead cost of threads for every
    call of `simulate_pool()` (unlike the equivalent for the naive
    thread solution). Also, errors raised in ThreadPoolExecutor get
    reraised in the main process, unlike in threads.
    One problem though is that we have to define the max number of
    threads in advance with the `max_workers` arg.

    In practice, this function seems to be about twice as fast as
    `run_game_threaded()`.

    Args:
        width (int): width of game board.
        height (int): height of game board.
    """
    start_time = time.time()
    grid = LockedGrid(width=width, height=height)
    grid = generate_grid1(width=width, height=height, grid=grid)
    print(grid.__str__())
    print(grid.height)
    with ThreadPoolExecutor(max_workers=10) as pool:
        for _ in range(STEP_COUNT):
            grid = simulate_pool(pool, grid=grid)
    end_time = time.time()
    print(f"Total time taken for ThreadPoolExecutor: {end_time-start_time:.3} seconds.")


def run_game_coroutine(width: int, height: int):
    start_time = time.time()
    grid = LockedGrid(width=width, height=height)
    grid = generate_grid1(width=width, height=height, grid=grid)
    for _ in range(STEP_COUNT):
        grid = asyncio.run(simulate_coroutine(grid=grid))
    end_time = time.time()
    print(f"Total time taken for RunGameCoroutine: {end_time-start_time:.3} seconds.")
