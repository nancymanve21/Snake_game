from turtle import Turtle
ALIGN = "center"
FONT = ("Aria", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", False, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over : {self.score}", False, align=ALIGN, font=FONT)

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()






