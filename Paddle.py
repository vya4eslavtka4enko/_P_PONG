from turtle import Turtle


class Puddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.goto(370, 0)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_pos_y = self.ycor() + 20
        self.goto(self.xcor(), new_pos_y)

    def go_down(self):
        new_pos_y = self.ycor() - 20
        self.goto(self.xcor(), new_pos_y)
