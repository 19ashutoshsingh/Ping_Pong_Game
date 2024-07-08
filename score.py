from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Courier", 25, "normal"))
        self.goto(-150, 250)
        self.write("Player 1", align="center", font=("Courier", 25, "normal"))
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Courier", 25, "normal"))
        self.goto(150, 250)
        self.write("Player 2", align="center", font=("Courier", 25, "normal"))

    def update_score(self):
        self.clear()
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Courier", 25, "normal"))
        self.goto(-150, 250)
        self.write("Player 1", align="center", font=("Courier", 25, "normal"))
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Courier", 25, "normal"))
        self.goto(150, 250)
        self.write("Player 2", align="center", font=("Courier", 25, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over...", align="center", font=("Courier", 25, "normal"))
