from turtle import Screen
import time
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
from snake import Snake
from food import Food
cory = Snake()
apple = Food()
cory.tail()
cory.move()
cory.tail()
cory.move()
cory.tail()
cory.move()
screen.onkey(cory.left,"Left")
screen.onkey(cory.right,"Right")
screen.onkey(cory.up,"Up")
screen.onkey(cory.down,"Down")
screen.listen()
play = 1
while play == 1:
    screen.update()
    time.sleep(0.1)
    cory.move()
    if cory.segment[0].distance(apple) < 15:
        apple.repos()
        cory.tail()
    if abs(cory.segment[0].xcor())>280 or abs(cory.segment[0].ycor())>280:
        play=0
    for i in cory.segment[1:]:
        if cory.segment[0].distance(i) < 10:
            play = 0

screen.exitonclick()