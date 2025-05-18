from window import Point, Line

class Cell():
    def __init__(self, top_left_point, bottom_right_point, win):
        self._x1 = top_left_point.x
        self._y1 = top_left_point.y
        self._x2 = bottom_right_point.x
        self._y2 = bottom_right_point.y
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.mid_point = Point((self._x1 + self._x2) // 2, \
                               (self._y1 + self._y2) // 2)
        self.visited = False
        self._win = win
    
    def draw(self, fill_color="black"):
        p1 = Point(self._x1, self._y1)
        p2 = Point(self._x1, self._y2)
        p3 = Point(self._x2, self._y1)
        p4 = Point(self._x2, self._y2)
        l1 = Line(p1, p2) if self.has_left_wall else Line(p1, p2, "white")
        l2 = Line(p1, p3) if self.has_top_wall else Line(p1, p3, "white")
        l3 = Line(p2, p4) if self.has_bottom_wall else Line(p2, p4, "white")
        l4 = Line(p4, p3) if self.has_right_wall else Line(p4, p3, "white")
        for line in [l1, l2, l3, l4]:
            if not self._win:
                return
            self._win.draw_line(line)


    def draw_move(self, to_cell, undo=False):
        connecting_line = Line(self.mid_point, to_cell.mid_point, "gray") if undo \
                          else Line(self.mid_point, to_cell.mid_point, "red")
        self._win.draw_line(connecting_line)