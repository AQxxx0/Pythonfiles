from turtle import  Turtle


class Paddle(Turtle):

    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.penup()
        self.goto(x,y)
        self.setheading(180)
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        newy = self.ycor() + 35
        self.goto(self.xcor(), newy)

    def go_down(self):
        newy = self.ycor() - 35
        self.goto(self.xcor(), newy)