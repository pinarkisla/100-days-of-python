from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write("Score: {score} ".format(score=self.score), align="center", font=("Arial", 15, "normal"))
        self.hideturtle()

    def new_score(self):
        self.score += 1
        self.clear()
        self.write("Score: {score} ".format(score=self.score), align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 30, "normal"))