import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car=CarManager()
score=Scoreboard()



screen.listen()
screen.onkey(player.moveup,'Up')
screen.onkey(player.movedown,'Down')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.makecars()
    car.carmove()
    for cars in car.allcars:
        if player.distance(cars)<25:
            game_is_on=False
            score.gameover()


        if player.ycor()>280:
            player.resets()
            car.carspeed()
            score.levelup()









screen.exitonclick()