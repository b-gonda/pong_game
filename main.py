from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=800)
screen.title("Pong game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.ball_moving()

    if ball.ycor() < -260 or ball.ycor() > 260:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 340:
        ball.reset_ball()
        scoreboard.add_score_left()
    elif ball.xcor() < -340:
        ball.reset_ball()
        scoreboard.add_score_right()

screen.exitonclick()
