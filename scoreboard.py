from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as f:
            self.highest_score = int(f.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def highest_scoreboard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highest_score))


    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", move=False, align=ALIGNMENT, font=FONT)

    def score_counter(self):
        self.score += 1
        self.highest_scoreboard()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
