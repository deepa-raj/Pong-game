from turtle import Screen, Turtle

# STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        # paddle = Turtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)





    # def create_paddle(self):
    #     for position in STARTING_POSITION:
    #         self.add_segment(position)
    #
    # def add_segment(self, position):
    #     new_segment = Turtle("square")
    #     new_segment.color("white")
    #     new_segment.penup()
    #     new_segment.goto(position)
    #     # self.segments.append(new_segment)