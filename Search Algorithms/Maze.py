'''
Author:     Nate Sommer
Topic:      Solve Maze with DFS, BFS, and A* Algorithms
Date:       8 November 2021
'''
###############################################################################
###############################################################################

from Stack import *
from Queue import *
from PriorityQueue import *
import copy
from enum import Enum
from typing import List, NamedTuple, Optional
import random

###############################################################################
###############################################################################

class Contents(str, Enum):
    ''' create an enumeration to define what the visual contents of a Cell are;
        using str as a "mixin" forces all the entries to be strings; using an
        enum means no cell entry can be anything other than the options here
    '''
    EMPTY   = " "
    START   = "@"
    GOAL    = "$"
    BLOCKED = "X"
    PATH    = "*"

###############################################################################
###############################################################################

class Position(NamedTuple):

    row: int
    col: int

###############################################################################
###############################################################################

class Cell:
    ''' allows us to use Cell as a data type -- an ordered triple of
        row, column, cell contents '''

    ##########
    def __init__(self, row: int, col: int, contents: Contents):
        self._position = Position(row, col)
        self._contents = contents

    ##########
    def get_position(self) -> Position:
        return Position(self._position.row, self._position.col)

    ##########
    def mark_on_path(self) -> None:
        self._contents = Contents.PATH

    ##########
    def is_blocked(self) -> bool:
        return self._contents == Contents.BLOCKED

    ##########
    def is_goal(self) -> bool:
        return self._contents == Contents.GOAL

    ##########
    def __str__(self) -> str:
        contents = "[EMPTY]" if self._contents == Contents.EMPTY else self._contents
        return f"({self._position.row}, {self._position.col}): {contents}"

    ##########
    def __eq__(self, other) -> bool:
        return self._position.row == other._position.row and \
               self._position.col == other._position.col and \
               self._contents == other._contents

###############################################################################
###############################################################################

class Node:

    ##########
    def __init__(self, cell: Cell, parent: Optional['Node'], cost: float, heuristic: float):
        self.cell       = cell
        self.parent     = parent
        self.cost       = cost
        self.heuristic  = heuristic

    ##########
    def __str__(self):
        parent = "None" if self.parent is None else self.parent.cell
        return f"{self.cell} : parent = {parent}"

    ##########
    def __lt__(self, other: 'Node') -> bool:
        return self.cost + self.heuristic < other.cost + other.heuristic

###############################################################################
###############################################################################

def manhattan(from_: Cell, to_: Cell) -> float:
    ''' Heuristic function for A* algorithm '''

    col_distance = abs(to_.get_position().col - from_.get_position().col)
    row_distance = abs(to_.get_position().row - from_.get_position().row)
    return col_distance + row_distance

###############################################################################
###############################################################################

class Maze:
    ''' class representing a 2D maxe of Cell objects '''

    _order = 0

    ##########
    def __init__(self, rows: int = 10, cols: int = 10, prop_blocked: float = 0.2, \
                       start: Position = Position(0, 0), \
                       goal:  Position = Position(9, 9) ):
        '''
        Args:
            rows:          number of rows in the grid
            cols:          number of columns in the grid
            prop_blocked:  proportion of cells to be blocked
            start:         tuple indicating the (row,col) of the start cell
            goal:          tuple indicating the (row,col) of the goal cell
        '''
        self._num_rows = rows
        self._num_cols = cols
        self._start    = Cell(start.row, start.col, Contents.START)
        self._goal     = Cell(goal.row,  goal.col,  Contents.GOAL)
        self._search_count = 0

        self._grid: List[List[Cell]] = \
            [ [Cell(r,c, Contents.EMPTY) for c in range(cols)] for r in range(rows) ]

        self._grid[start.row][start.col] = self._start
        self._grid[goal.row][goal.col]   = self._goal

        options = [cell for row in self._grid for cell in row]
        options.remove(self._start)
        options.remove(self._goal)
        blocked = random.sample(options, k = round((rows * cols - 2) * prop_blocked))
        for b in blocked: b._contents = Contents.BLOCKED

    ##########
    def __str__(self) -> str:
        ''' returns a str version of the maze, showing contents, with cells
            deliminted by vertical pipes '''
        maze_str = ""
        for row in self._grid:
            maze_str += "|" \
                + "|".join([f"{int(cell._contents):2}" if not isinstance(cell._contents, str) else \
                            f"{cell._contents:2}" for cell in row]) + "|\n"
        return maze_str[:-1]

    ##########
    def get_start(self): return self._start

    ##########
    def get_goal(self):  return self._goal

    ##########
    def get_search_locations(self, cell: Cell) -> List[Cell]:
        ''' return a list of Cell objects of valid places to explore
        Args:
            cell: the current cell being explored
        Returns:
            a list of valid Cell objects for further exploration
        '''
        valid_cells = []
        locations = []

        if cell._position.row != 0:
            locations.append(self._grid[cell._position.row-1][cell._position.col])
        if cell._position.row+1 != self._num_rows:
            locations.append(self._grid[cell._position.row+1][cell._position.col])
        if cell._position.col != 0:
            locations.append(self._grid[cell._position.row][cell._position.col-1])
        if cell._position.col+1 != self._num_cols:
            locations.append(self._grid[cell._position.row][cell._position.col+1])

        for location in locations:
            if location.is_blocked() is False:
                valid_cells.append(location)

        return valid_cells

    ##########
    def dfs(self) -> Optional[Node]:
        '''
        Use DFS + stack:
            stack: push new Nodes (wrappers around cells) to be explored
                    which will also keep track of the parent
            list:  cells already explored
        Return:
            current node if it is the goal
            None, if no goal can be found
        '''
        stack = Stack()
        stack.push(Node(self._start, None, None, None))

        explored_list = [self._start]

        try:
            while not stack.is_empty():
                node = stack.pop()
                for loc in self.get_search_locations(node.cell):
                    if loc not in explored_list:
                        self._search_count += 1
                        stack.push(Node(loc, node, None, None))
                        explored_list.append(node.cell)
                        if loc == self._goal: return Node(self._goal, node, None, None), self._search_count
        except:
            return None

    ##########
    def bfs(self) -> Optional[Node]:
        '''
        Use BFS + queue:
            queue: push new Nodes (wrappers around cells) to be explored
                    which will also keep track of the parent
            list:  cells already explored
        Return:
            current node if it is the goal
            None, if no goal can be found
        '''
        queue = Queue()
        queue.push(Node(self._start, None, None, None))

        explored_list = [self._start]

        try:
            while not queue.is_empty():
                node = queue.pop()
                for loc in self.get_search_locations(node.cell):
                    if loc not in explored_list:
                        self._search_count += 1
                        queue.push(Node(loc, node, None, None))
                        explored_list.append(node.cell)
                        if loc == self._goal: return Node(self._goal, node, None, None), self._search_count
        except:
            return None

    ##########
    def a_star(self) -> Optional[Node]:
        to_explore = PriorityQueue()
        explored = {}

        n = self._start
        g_n = 0.0
        h_n = manhattan(self._start, self._goal)
        f_n = g_n + h_n

        to_explore.insert(f_n, Node(n, None, g_n, h_n))
        explored[n._position] = g_n

        while not to_explore.is_empty():
            e = to_explore.remove_min()
            n = e._value
            if n.cell == self._goal: return n, self._search_count

            for m in self.get_search_locations(n.cell):
                g_m = g_n + 1
                if m._position not in explored.keys() or g_m < explored[m._position]:
                    self._search_count += 1
                    explored[m._position] = g_m
                    h_m = manhattan(m, self._goal)
                    f_m = g_m + h_m
                    to_explore.insert(f_m, Node(m, n, g_m, h_m))

    ##########
    def show_path(self, node: Node) -> None:
        path = []
        while node.parent is not None:
            path.append(node.cell)
            node = node.parent
        path.append(node.cell)

        path.reverse()

        for cell in path:
            if cell != self._start and cell != self._goal:
                cell.mark_on_path()
        print(self)

    ##########
    def path_length(self, node: Node) -> int:

        path = []

        while node.parent is not None:

            path.append(node.cell)
            node = node.parent

        path.append(node.cell)

        return len(path)

    ##########
    def is_path_same(self, other, node, other_node) -> bool:

        path  = []
        path2 = []

        while node.parent is not None:

            path.append(node.cell)
            node = node.parent

        path.append(node.cell)

        while other_node.parent is not None:

            path2.append(other_node.cell)
            other_node = other_node.parent

        path2.append(other_node.cell)

        return path == path2

###############################################################################
###############################################################################

def make_10x10_maze() -> Maze:
    ''' creates a maze like that shown in slides 28-32 of day 27 slides
    Returns:
        a Maze object
    '''
    rows = 10
    cols = 10
    p = 0

    maze = Maze(rows, cols, start = Position(0,0), \
                            goal = Position(rows-1,cols-1), prop_blocked = p)

    blocks = [(0,5),(0,7),(1,1),(2,7),(3,1),(3,2),(3,9),(4,2),(5,2),(5,5),(6,1),(8,5),(8,9)]
    for r,c in blocks:
        maze._grid[r][c]._contents = Contents.BLOCKED

    return maze

###############################################################################
###############################################################################

def one_experiment(maze: Maze, show: bool = False) -> list:

    dfs = maze.dfs()

    while dfs is not None:

        maze_dfs   = copy.deepcopy(maze)
        maze_bfs   = copy.deepcopy(maze)
        maze_astar = copy.deepcopy(maze)

        dfs        = maze_dfs.dfs()
        dfs_goal   = dfs[0]
        dfs_size   = dfs[1]
        dfs_length = maze_dfs.path_length(dfs_goal)

        bfs        = maze_bfs.bfs()
        bfs_goal   = bfs[0]
        bfs_size   = bfs[1]
        bfs_length = maze_bfs.path_length(bfs_goal)

        a_star        = maze_astar.a_star()
        a_star_goal   = a_star[0]
        a_star_size   = a_star[1]
        a_star_length = maze_astar.path_length(a_star_goal)

        search_size = [dfs_size, bfs_size, a_star_size]
        path_length = [dfs_length, bfs_length, a_star_length]

        if show == True:
            print()
            maze_dfs.show_path(dfs_goal)
            print()
            maze_bfs.show_path(bfs_goal)
            print()
            maze_astar.show_path(a_star_goal)
            print()

        return [search_size, path_length, a_star_length == bfs_length, \
                    maze_dfs.is_path_same(maze, bfs_goal, a_star_goal)]

    else: return 'NO MAZE SOLUTION'

###############################################################################
###############################################################################

def main():

    for i in range(30):

        row = random.randint(5,10)
        col = random.randint(5,10)
        maze = Maze(row, col, 0.2, start = Position(0,0), goal = Position(row-1,col-1))
        print(one_experiment(maze, show = True))
        print()

    #####################################
    '''
    maze = make_10x10_maze()
    print(maze)
    print()

    goal_node = maze.dfs()
    if goal_node is not None:
        maze.show_path(goal_node)
    else:
        print("No solution using DFS")
    print()

    #####################################

    maze = make_10x10_maze()

    goal_node = maze.bfs()
    if goal_node is not None:
        maze.show_path(goal_node)
    else:
        print("No solution using BFS")
    print()

    #####################################

    maze = make_10x10_maze()

    goal_node = maze.a_star()
    if goal_node is not None:
        maze.show_path(goal_node)
    else:
        print("No solution using A*")
    print()
    '''
###############################################################################
###############################################################################

if __name__ == '__main__':
    main()
