from turtle import Turtle
MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.posit = pos
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor()+MOVE_DISTANCE)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor()-MOVE_DISTANCE)

