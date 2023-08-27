from turtle import Turtle
class Snake:
    segment = []
    def tail(self):
        tail = Turtle()
        tail.penup()
        tail.shape("square")
        tail.color("black")
        if len(self.segment) != 0:
            tail.goto(self.segment[-1].xcor(),self.segment[-1].ycor())
        tail.color("yellow")
        tail.speed("fastest")
        self.segment.append(tail)

    def move(self):
        for i in range (len(self.segment)-1,0,-1):
            if i == len(self.segment)-1 and self.segment[i].pos() == self.segment[i-1].pos():
                continue
            self.segment[i].goto(self.segment[i-1].pos())
        self.segment[0].forward(20)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)
