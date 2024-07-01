from turtle import Turtle, Screen
STARTING_POSITION = [(0,0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        timmy = Turtle()
        timmy.shape("square")
        timmy.color("green")
        timmy.penup()
        timmy.goto(position)
        self.segments.append(timmy)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for segs in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segs - 1].xcor()
            new_y = self.segments[segs - 1].ycor()
            self.segments[segs].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:

            self.head.setheading(RIGHT)



