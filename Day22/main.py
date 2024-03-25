from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
# from line import Line
import time

# Screen configs
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create objects
l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)
ball = Ball()
score = Score()

# Screen actions
screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    score.update_score

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.gol()
        score.l_gol()

    if ball.xcor() < -380:
        ball.gol()
        score.r_gol()


screen.exitonclick()
