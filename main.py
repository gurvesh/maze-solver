from window import Window, Point, Line
from cell import Cell
from maze import Maze

win = Window(1000, 1000)
# p1 = Point(2,2)
# p2 = Point(100,100)
# l1 = Line(p1, p2)
# win.draw_line(l1, "red")
# cell1 = Cell(p1, p2, win)
# cell1.draw("green")

# p3 = Point(5,5)
# p4 = Point(10,10)
# cell2 = Cell(p3, p4, win)
# cell2.has_left_wall = False
# cell2.draw("purple")
# cell1.draw_move(cell2)

maze1 = Maze(
    x1=10,
    y1=10,
    num_rows=40,
    num_cols=40,
    cell_size_x=20,
    cell_size_y=20,
    win=win
)

maze1.solve()


win.wait_for_close()