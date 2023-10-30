from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce_y(self):
        # self.x_cor *= 1
        self.y_cor *= -1
    def bounce_x(self):
         self.x_cor *= -1
        # self.y_cor *= -1
         self.ball_speed*=0.9
    def reset_position(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        self.bounce_x()