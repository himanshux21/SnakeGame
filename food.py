from turtle import Turtle
import random
from new_snake import Snake
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.refresh()
    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.color(self.colormode())
    def colormode(self):
        r = random.randint(70, 150)
        g = random.randint(70, 150)
        b = random.randint(70, 150)
        colors = (r, g, b)
        return colors
