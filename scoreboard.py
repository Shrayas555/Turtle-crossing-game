from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230,260)
        self.level=1

        self.write(f'Level : {self.level}',align='center',font = FONT)
    def levelup(self):
        self.clear()
        self.level+=1
        self.write(f'Level : {self.level}', align='center', font=FONT)
    def gameover(self):

        self.hideturtle()
        self.goto(0,0)
        self.write('GAME OVER ', align='center', font=FONT)

