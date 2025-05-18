from window import Point, Line
from cell import Cell
import time
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self.seed = random.seed(seed) if seed else 0
        self._create_cells()
        self._break_entrance_and_exit()
        self.break_walls_r((0,0))
        self.reset_cells_visited()
        # self.solve()

    def _create_cells(self):
        self._cells = [[Cell(Point(self.x1 + j*self.cell_size_x, self.y1 + i*self.cell_size_y), \
                             Point(self.x1 + (j+1)*self.cell_size_x, self.y1 + (i+1)*self.cell_size_y), \
                            self.win) for j in range(self.num_cols)] for i in range(self.num_rows)]
        self._draw_cells()
    
    def _draw_cells(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].draw()
                
        self._animate()
    
    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        # time.sleep(0.002)

    def _break_entrance_and_exit(self):
        top_left_cell = self._cells[0][0]
        bottom_right_cell = self._cells[self.num_rows-1][self.num_cols-1]
        top_left_cell.has_top_wall = False
        top_left_cell.draw()
        bottom_right_cell.has_bottom_wall = False
        bottom_right_cell.draw()

    def neighbours(self, coords):
        i, j = coords
        neighbour_coords = [
            (i+1, j),
            (i, j+1),
            (i-1, j),
            (i, j-1)
        ]
        return [(i1, j1) for (i1, j1) in neighbour_coords \
                    if i1 >= 0  \
                    and i1 < self.num_rows \
                    and j1 >= 0 \
                    and j1 < self.num_cols]
    
    def break_walls_r(self, start_cell_coords):
        i, j = start_cell_coords
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            unvisited_neighbours = [(i1, j1) for (i1, j1) in self.neighbours((i, j)) \
                                    if not self._cells[i1][j1].visited]
            if unvisited_neighbours == []:
                current_cell.draw()
                return
            i1, j1 = random.choice(unvisited_neighbours)
            # print(f"all: {unvisited_neighbours}, chosen: {i1, j1}")
            new_cell = self._cells[i1][j1]
            if i1 - i == 1:
                current_cell.has_bottom_wall = False
                new_cell.has_top_wall = False
            elif i - i1 == 1:
                current_cell.has_top_wall = False
                new_cell.has_bottom_wall = False
            elif j1 - j == 1:
                current_cell.has_right_wall = False
                new_cell.has_left_wall = False
            else:                
                current_cell.has_left_wall = False
                new_cell.has_right_wall = False
            current_cell.draw()
            self._animate()
            self.break_walls_r((i1, j1))

    def reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r((0,0))
    
    def _solve_r(self, coords):
        self._animate()
        i, j = coords
        current_cell = self._cells[i][j]
        current_cell.visited = True
        unvisited_neighbours = [(i1, j1) for (i1, j1) in self.neighbours((i, j)) \
                                    if not self._cells[i1][j1].visited]
        for (i1, j1) in unvisited_neighbours:
            new_cell = None
            if (i1 - i == 1 and current_cell.has_bottom_wall == False) or \
                (i1 - i == -1 and current_cell.has_top_wall == False) or \
                (j1 - j == 1 and current_cell.has_right_wall == False) or \
                (j1 - j == -1 and current_cell.has_left_wall == False):

                new_cell = self._cells[i1][j1]            
                current_cell.draw_move(new_cell)
                if (i1, j1) == (self.num_rows-1, self.num_cols-1) or self._solve_r((i1, j1)):
                    return True
            if new_cell:
                current_cell.draw_move(new_cell, undo=True)
        return False