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

STARTING_MOVE_PACE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.pace = STARTING_MOVE_PACE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = t.Turtle("square")
            t.colormode(255)
            new_car.color(random.choice(rgb_colors))
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def move_horizontally(self):
        for car in self.all_cars:
            car.backward(self.pace)

    def level_up(self):
        self.pace += MOVE_INCREMENT
        self.move_horizontally()



