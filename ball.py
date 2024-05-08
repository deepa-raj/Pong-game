from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



# #
# position of the ball. But effectively,
#
# all that we're doing is we're defining an amount that the ball is going to move
#
# by in the X and the Y axis.
#
# We're adding that amount to the X and Y coordinates in order to move the ball.
#
# And when the ball needs to bounce off the top and bottom walls,
#
# we reverse the y_move number so that we get it to subtract instead of add.
#
# And that moves it in the opposite direction.


