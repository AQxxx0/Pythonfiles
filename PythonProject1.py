from turtle import  Turtle , Screen
from random import *


isRaceon = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput("make ur bet ", "Which turtle will win the race")


timmy = Turtle("turtle")
tommy = Turtle("turtle")
jack = Turtle("turtle")
alphes  = Turtle("turtle")
tur = Turtle("turtle")
bure =Turtle("turtle")


timmy.color("black") ; tommy.color("blue"); jack.color("red") ; alphes.color("green"); tur.color("purple") ; bure.color("pink")
timmy.name = "timmy";  tommy.name = "tommy" ; bure.name = "bure" ; jack.name = "jack" ; alphes.name = "alphes" ; tur.name = "turtle"
y = -80


for turtle in (timmy, tommy, jack, alphes, tur, bure):
    turtle.penup()
    turtle.goto(-250,y)
    y = y +35

if user_input:
    isRaceon = True
else:
    isRaceon = False

winner = None
while  isRaceon:
    for turtle in (timmy, tommy, jack, alphes, tur, bure):
        turtle.forward(randint(10,80))
        if turtle.xcor() >= 250:
            winner = turtle.name
            if user_input == winner:
                print(f"You guessed correctly , Winner is {winner}")
                isRaceon = False

            else:
                print(f"Wrong guess Loser {user_input} lost")
                isRaceon = False


            break









screen.exitonclick()

