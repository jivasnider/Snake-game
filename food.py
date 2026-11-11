from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.penup()
        self.refresh()

    def refresh(self):
        x_cord = random.randrange(-280, 280, 20)
        y_cord = random.randrange(-280, 280, 20)
        self.goto(x_cord, y_cord)
