import turtle
turtle.addshape("Heart.gif")


class Life(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Heart.gif")
        self.penup()
        self.goto(x, y)

    def jump(self):
        """
        remove heart out of player sight
        """
        self.goto(600, 600)