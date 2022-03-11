import turtle
import random
turtle.addshape("mole2.gif")


class Food(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("mole2.gif")
        self.penup()
        self.goto(random.randint(-190, 190), random.randint(-190, 190))

    def jump(self):
        """
        move object to random position
        """
        self.goto(random.randint(-190, 190), random.randint(-190, 190))
        self.setheading(random.randint(0, 360))