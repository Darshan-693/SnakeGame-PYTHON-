from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("black")
        x = random.randint(-200,200)
        y = random.randint(-200, 200)
        self.goto(x,y)
        self.color("red")
        self.repos()
    def repos(self):
        self.color("black")
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self.goto(x, y)
        self.color("red")