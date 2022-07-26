from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.points_left = 0
        self.points_right = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write("Liczba punktow {} : {}".format(self.points_left, self.points_right), move=False, align=ALIGNMENT, font=FONT)

    def add_score_left(self):
        self.points_left += 1
        self.clear()
        self.update_scoreboard()

    def add_score_right(self):
        self.points_right += 1
        self.clear()
        self.update_scoreboard()