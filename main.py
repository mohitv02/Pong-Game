from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
screen.update()
screen.listen()

ball = Ball()
screen.onkey(paddle1.move_up, "Up")
screen.onkey(paddle1.move_down, "Down")
screen.onkey(paddle2.move_up, "w")
screen.onkey(paddle2.move_down, "s")
score = Scoreboard()
game_is_on = True
x = 0

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(paddle1) < 50 or ball.xcor() < -320 and ball.distance(paddle2) < 50:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        score.ll_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.rr_point()


screen.exitonclick()
