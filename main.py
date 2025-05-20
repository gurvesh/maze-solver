from window import Window, Point, Line, My_button
from cell import Cell
from maze import Maze

win = Window(900, 900)
maze = None

create_maze_button = My_button("Create maze", win)
but1 = My_button("Solve", win)
but2 = My_button("Reset", win)

def create_maze():
    global maze, win, but1, but2, create_maze_button
    win.canvas.delete("all")
    win.redraw()
    try:
        num_rows = min(int(win.num_rows_var.get()), 40)
        num_cols = min(int(win.num_cols_var.get()), 40)
    except Exception as e:
        print(e)
    cell_width = (win.canvas.winfo_width() // num_cols) - 2
    cell_height = (win.canvas.winfo_height() // num_rows) - 2
    maze = Maze(
        x1=10,
        y1=10,
        num_rows=num_rows,
        num_cols=num_cols,
        cell_size_x=cell_width,
        cell_size_y=cell_height,
        win=win
    )
    but1.button.configure(command=maze.solve)
    but2.button.configure(command=maze.redraw)

create_maze_button.button.configure(command=create_maze)

win.wait_for_close()