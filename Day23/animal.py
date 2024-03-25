from turtle import Turtle

class Animal(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

    def move_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 20, self.ycor())

    def level_up(self):
        self.goto(0, -280)