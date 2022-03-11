import turtle


class Score(turtle.Turtle):
    def __init__(self, name, highest_score):
        turtle.Turtle.__init__(self)
        self.name = name.capitalize()
        self.life = 5
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_round = []
        self.score = 0
        self.high_score = highest_score
        self.update_score()

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, s):
        if not isinstance(s, int):
            raise TypeError("Score must be int")
        self.__score = s

    @property
    def high_score(self):
        return self.__high_score

    @high_score.setter
    def high_score(self, hs):
        if not isinstance(hs, int):
            raise TypeError("Score must be int")
        self.__high_score = hs

    def update_score(self):
        self.clear()
        self.goto(13, 260)
        self.write(("Score: {} High Score: {}".format(self.score, self.high_score)), font=("Copperplate", 20, "normal"))
        self.goto(-250, 260)
        self.write(self.name, move=False, align="center", font=("Copperplate", 20, "normal"))



