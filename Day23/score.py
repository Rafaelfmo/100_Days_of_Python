from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=('Courier',24, 'normal'))
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Courier',24, 'normal'))

