
# TODO 1: Create the screen
# TODO 2: Create and move a paddle
# TODO 3:Create another paddle
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle
# TODO 7:Detect when paddle misses
# TODO 8:Keep score


from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# let's say I wanted you to create a top paddle for some reason,
#
# then all I have to do is just call the paddle class and then pass in a tuple
#
# for the location of this paddle.




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()


    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -360:
        # needs to bounce
        ball.bounce_x()


    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()