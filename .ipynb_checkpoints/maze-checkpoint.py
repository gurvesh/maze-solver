from window import Point, Line
from cell import Cell
import time

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

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
        time.sleep(0.05)

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
            (i-1, j),
            (i+1, j),
            (i, j-1),
            (i, j+1)
        ]
        neighbour_coords = [(i1, j1) for (i1, j1) in neighbour_coords \
                                if i1 >= 0  \
                                and i1 < self.num_rows \
                                and j1 >= 0 \
                                and j1 < self.num_cols]