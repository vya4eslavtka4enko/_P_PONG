from turtle import Turtle, Screen
from Paddle import Puddle
from Ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
r_puddle = Puddle((350, 0))
l_puddle = Puddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(r_puddle.go_up, 'Up')
screen.onkey(r_puddle.go_down, 'Down')
screen.onkey(l_puddle.go_up, 'w')
screen.onkey(l_puddle.go_down, 's')
score = Scoreboard()
score.update_score()
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    if ball.distance(r_puddle) < 50 and ball.xcor() > 320 or ball.distance(l_puddle) < 50 and ball.xcor() > -360:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score_increase()
        score.update_score()
    elif ball.xcor() < -380:
        ball.reset_position()
        score.update_score()
        score.r_score_increase()
        score.update_score()
screen.exitonclick()
