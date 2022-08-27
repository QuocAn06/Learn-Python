from turtle import Turtle
import random

FOOD_SIZE = 0.5
FOOD_COLOR = "red"


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=FOOD_SIZE, stretch_wid=FOOD_SIZE)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
