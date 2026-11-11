from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment_list = []

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
FORWARD = 20


class Snake:

    def __init__(self):
        for position in starting_position:
            self.segment = Turtle("square")
            self.segment.color("white")
            self.segment.penup()
            self.segment.goto(position)
            segment_list.append(self.segment)
            self.head = segment_list[0]

    def move(self):
        global x_cord, y_cord
        for seg in range(len(segment_list) - 1, 0, -1):
            x_cord = segment_list[seg - 1].xcor()
            y_cord = segment_list[seg - 1].ycor()
            segment_list[seg].goto(x=x_cord, y=y_cord)
        self.head.forward(FORWARD)

    def extend(self):
        self.new_segment = Turtle("square")
        self.new_segment.color("white")
        self.new_segment.penup()
        self.new_segment.goto(x=x_cord, y=y_cord)
        segment_list.append(self.new_segment)

    def tail_collision(self):
        for i in segment_list[1:-1]:
            if self.head.distance(i) <  10:
                return True

    def go_north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
