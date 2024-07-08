from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# line = Turtle()
# line.color("white")
# line.speed("fastest")
# line.hideturtle()
# line.goto(0, -300)
# line.goto(0, 300)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")

screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "z")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # collision with walls(up and down)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddles
    if ball.distance(r_paddle) < 30 or ball.distance(l_paddle) < 30:
        ball.bounce_x()

    # collision with walls(up and down)
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_pos()
        ball.ball_speed += 0.2

    if ball.xcor() < -385:
        score.r_point()
        ball.reset_pos()
        ball.ball_speed += 0.25

    if score.l_score > 5 or score.r_score > 5:
        game_is_on = False
        score.game_over()
        # print(ball.ball_speed)


screen.exitonclick()
