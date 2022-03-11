import turtle


class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.color("brown")
        self.pensize(4)

    def draw_border(self):
        self.penup()
        self.goto(-200, -200)
        self.pendown()
        self.goto(-200, 200)
        self.goto(200, 200)
        self.goto(200, -200)
        self.goto(-200, -200)