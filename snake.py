import turtle
import math

turtle.addshape("snake2.gif")


class Snake(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("snake2.gif")
        self.penup()
        self.goto(0, 0)
        self.direction = "stop"

    def move(self):
        if self.direction == "up":
            y = self.ycor()
            self.sety(y + 20)
            self.direction = "up"
        if self.direction == "down":
            y = self.ycor()
            self.sety(y - 20)
            self.direction = "down"
        if self.direction == "right":
            x = self.xcor()
            self.setx(x + 20)
            self.direction = "right"
        if self.direction == "left":
            x = self.xcor()
            self.setx(x - 20)
            self.direction = "left"

    # all functions below is to set direction and use for onkey()
    def turn_left(self):
        self.direction = "left"

    def turn_right(self):
        self.direction = "right"

    def go_up(self):
        self.direction = "up"

    def go_down(self):
        self.direction = "down"

    def eat(self, other):
        """
        check if the snake go near the other object
        :param other: Food class
        :return: boolean
        """
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        c = math.sqrt((a ** 2) + (b ** 2))
        if c < 35:
            return True
        else:
            return False

    def hit_border(self):
        """
        check if the snake hit the border
        :param other: Border class
        :return: boolean
        """
        if self.xcor() > 190 or self.xcor() < -190:
            return True
        if self.ycor() > 190 or self.ycor() < -190:
            return True