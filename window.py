from tkinter import Tk, BOTH, Canvas, Button, Frame, Label, Entry, StringVar

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        # self.root.geometry(f"{width}x{height}")
        self.root.title("Python Maze Solver")
        self.root.configure(bg="white")
        self.canvas = Canvas(width=width, height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=1)
        self.window_running = False

        self.num_rows_var = StringVar()
        self.num_cols_var = StringVar()
        self.size_input_frame1 = Frame(self.root)
        self.lab1 = Label(self.size_input_frame1, width=20, text='Enter rows (max 40)', anchor='w')
        self.ent1 = Entry(self.size_input_frame1, textvariable=self.num_rows_var)
        self.size_input_frame2 = Frame(self.root)
        self.lab2 = Label(self.size_input_frame2, width=20, text='Enter cols (max 40)', anchor='w')
        self.ent2 = Entry(self.size_input_frame2, textvariable=self.num_cols_var)
        self.size_input_frame1.pack(side="left")
        self.size_input_frame2.pack(side="left")

        self.lab1.pack(side="left")
        self.ent1.pack(side="right")
        self.lab2.pack(side="left")
        self.ent2.pack(side="right")
        self.root.protocol("WM_DELETE_WINDOW", self.close)



    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line):
        line.draw(self.canvas)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2, color="black"):
        self.start = point1
        self.end = point2
        self.color = color

    def draw(self, canvas):
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        canvas.create_line(
            x1, y1, x2, y2, fill=self.color, width=2
        )

class My_button():
    def __init__(self, text, win, action=None):
        self.button = Button(win.root, text=text, command=action)
        self.button.pack()

    def reassign_action(self, action):
        self.button = Button()