from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):


        self.allcars=[]
        self.carss=STARTING_MOVE_DISTANCE


    def makecars(self):
        chance=random.randint(1,6)
        if chance==1:
            new=Turtle()
            new.penup()
            new.shape('square')
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.color(random.choice(COLORS))
            y=random.randint(-250,250)
            new.goto(300,y)
            self.allcars.append(new)

    def carmove(self):
        for i in self.allcars:
            i.backward(self.carss)
    def carspeed(self):
        self.carss+=10





