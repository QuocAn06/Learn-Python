from turtle import Turtle

SCOREBOARD_POSITION = (0, 270)
ALIGNMENT = "center"
SCORE_FONT = ('Courier', 14, 'bold')
GAME_OVER_FONT = ('Courier', 24, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.hideturtle()
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())

    def save_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


