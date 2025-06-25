from turtle import Screen , Turtle
from paddle2 import Paddle
from ball import Ball
from score  import ScoreB
import time






screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)


screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()

scoreBoared = ScoreB()

screen.listen()


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

scoreBoared.l_score = 0
scoreBoared.r_score = 0

game_is_on = True
while game_is_on:



    time.sleep(ball.move_speed)

    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()



    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()



    if ball.xcor() > 380 :
        ball.reset_position()
        scoreBoared.l_point()



    if ball.xcor() < -380 :
        ball.reset_position()
        scoreBoared.r_point()





    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()





screen.exitonclick()