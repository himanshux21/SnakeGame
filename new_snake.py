from turtle import Turtle, Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
Screen().colormode(255)


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for y in STARTING_POSITIONS:
            self.add_segment(y)
            self.segments[0].color('white')

    def add_segment(self, y):
        b = Turtle('square')
        b.color('white')
        b.penup()
        b.goto(y)
        self.segments.append(b)

    def extend_segment(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for x in range(len(self.segments)-1, 0, -1):
            if x-1 < 0:
                break
            else:
                pos = self.segments[x-1].pos()
                self.segments[x].goto(pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
