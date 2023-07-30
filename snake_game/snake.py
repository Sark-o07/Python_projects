import turtle as t
import random
rgb_colors =\
    [
              (176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38),
              (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89),
              (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202),
              (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79),
              (215, 207, 37), (52, 58, 66), (31, 87, 90), (76, 51, 43), (40, 67, 65), (84, 37, 55)
    ]
STARTING_XCOR = [(0, 0), (-20, 0), (-40, 0)]
STEP_COUNT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        self.segments = []
        self.start_color = "white"
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")

    def create_snake(self):
        for position in STARTING_XCOR:
            self.add_segment(position, self.start_color)

    def add_segment(self, position, segment_color):
        segment = t.Turtle("square")
        t.colormode(255)
        segment.color(segment_color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)



    def extend_segment(self):
        self.add_segment(self.segments[-1].position(), random.choice(rgb_colors))

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.fd(STEP_COUNT)

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