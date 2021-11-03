'''
Author:     Nate Sommer
Topic:      Using DFS and BFS to solve a maze
Date:       22 October 2021
'''
###############################################################################
###############################################################################

from Stack import *
from Queue import *
from copy import deepcopy
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
    BLOCKED = "░"
    PATH    = "*"

###############################################################################
###############################################################################

class Position(NamedTuple):
    ''' just allows us to use .row and .col rather than the less-easy-to-read
        [0] and [1] '''
    row: int
    col: int

###############################################################################
###############################################################################

class Cell:
    ''' allows us to use Cell as a data type -- an ordered triple of
        row, column, cell contents '''
    def __init__(self, row: int, col: int, contents: Contents):
        self._position = Position(row, col)
        self._contents = contents
    def get_position(self) -> Position:
        return Position(self._position.row, self._position.col)
    def mark_on_path(self) -> None:
        self._contents = Contents.PATH
    def is_blocked(self) -> bool:
        return self._contents == Contents.BLOCKED
    def is_goal(self) -> bool:
        return self._contents == Contents.GOAL
    def __str__(self) -> str:
        contents = "[EMPTY]" if self._contents == Contents.EMPTY else self._contents
        return f"({self._position.row}, {self._position.col}): {contents}"
    def __eq__(self, other) -> bool:
        return self._position.row == other._position.row and \
               self._position.col == other._position.col and \
               self._contents == other._contents

###############################################################################
###############################################################################

class Node:
    ''' Wrapper class around a cell to allow us to also keep track of the cell's
        parent when doing path exploration.  Notes:
             - the parent of the start cell will be None (hence, Optional below)
             - you should use instances of Node to push onto the stack in dfs
    '''
    def __init__(self, cell: Cell, parent: Optional['Node']):
        self.cell   : Cell             = cell
        self.parent : Optional['Node'] = parent

    def __str__(self):
        parent = "None" if self.parent is None else self.parent.cell
        return f"{self.cell} : parent = {parent}"

###############################################################################
###############################################################################

class Maze:
    ''' class representing a 2D maze of Cell objects '''

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

        self._grid: List[List[Cell]] = \
            [ [Cell(r,c, Contents.EMPTY) for c in range(cols)] for r in range(rows) ]

        self._grid[start.row][start.col] = self._start
        self._grid[goal.row][goal.col]   = self._goal

        options = [cell for row in self._grid for cell in row]
        options.remove(self._start)
        options.remove(self._goal)
        blocked = random.sample(options, k = round((rows * cols - 2) * prop_blocked))
        for b in blocked: b._contents = Contents.BLOCKED

    def __str__(self) -> str:
        ''' returns a str version of the maze, showing contents, with cells
            deliminted by vertical pipes '''
        maze_str = ""
        for row in self._grid:
            maze_str += "|" + "|".join([cell._contents for cell in row]) + "|\n"
        return maze_str[:-1]

    def get_start(self): return self._start
    def get_goal(self):  return self._goal

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

    def dfs(self) -> Node:
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
        stack.push(Node(self._start,None))

        explored_list = [self._start]

        try:
            while not stack.is_empty():
                node = stack.pop()
                for loc in self.get_search_locations(node.cell):
                    if loc not in explored_list:
                        stack.push(Node(loc,node))
                        explored_list.append(node.cell)
                        if loc == self._goal: return node
        except:
            return None

    def bfs(self) -> Node:
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
        queue.push(Node(self._start,None))

        explored_list = [self._start]

        try:
            while not queue.is_empty():
                node = queue.pop()
                for loc in self.get_search_locations(node.cell):
                    if loc not in explored_list:
                        queue.push(Node(loc,node))
                        explored_list.append(node.cell)
                        if loc == self._goal: return node
        except:
            return None

    def show_path(self, node: Node) -> None:
        ''' method to update the path from start to goal, identifying the steps
            along the way as belonging to the path (updating the cell via
            .mark_on_path, which will change that cell's ._contents to
            Contents.PATH), printing the final resulting solutions
        Args:
            node: a Node (wrapper of current cell and parent Node) corresponding
                  to the goal node
        Returns:
            None -- just updates the cells in the grid to identify those on the path
        '''
        path = []
        while node.parent is not None:
            path.append(node.cell)
            node = node.parent
        path.append(node.cell)

        path.reverse()

        for cell in path:
            if cell != self._start and cell != self._goal:
                cell.mark_on_path()

###############################################################################
###############################################################################

def main():

    random.seed(8675309)
    maze = Maze()
    
    #goal = maze.dfs()
    goal = maze.bfs()

    if goal != None:
        maze.show_path(goal)
        print(maze)
    else: print("NO PATH TO GOAL")

###############################################################################
###############################################################################

if __name__ == '__main__':
    main()
