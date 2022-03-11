# Snake Game

This snake game is like the old fashion game 
in the 90s accept I made some changes about it.
All modules are using method provide by turtle.

######This project use Python version 3.9 

## Modules

There are five modules to create this game

### 1. Module `snake.py`

This module contains the `Snake` class for
create snake's functions.

        
    class Snake(turtle.Turtle):
    def __init__(self):
        ...

    def move(self):
        ...

    def turn_left(self):
        ...

    def turn_right(self):
        ...

    def go_up(self):
        ...

    def go_down(self):
        ...

    def eat(self, other):
        ...

    def hit_boarder(self, other):
        ...

This first class use for create and move snake
in direction player want and check if the snake
eat object or collide with the border.

### 2. Module `food.py`
This module contains `Food` class to create
apple.

    class Food(turtle.Turtle):
    def __init__(self):
        ...

    def jump(self):
        ...

This module will initialize food to start 
randomly on the map. When use jump(), the food
will reappear randomly.

### 3. Module `border.py`
This module contains `Border` class to draw border
for the game.

    class Border(turtle.Turtle):
    def __init__(self):
        ...

    def draw_border(self):
        ...

### 4. Module `score.py`
This module contains `Score` class for the game 
to be able to keep the score from player and write 
the score on screen

    class Score(turtle.Turtle):
    def __init__(self, name, highest_score):
        ...

    def update_score(self):
        ...
    
### 5. Module `life.py`

This module contains `Life` class which will create
heart shape.

    class Life(turtle.Turtle):
    def __init__(self, x, y):
        ...

    def jump(self):
        ... 

Function jump() will remove heart from the window


## How to play this game
From `main.py`, the console to control the
snake is arrow `Right`, `Left`,`Up`, `Down` 

    screen.listen()
    screen.onkey(snake.turn_right, "Right")
    screen.onkey(snake.turn_left, "Left")
    screen.onkey(snake.go_up, "Up")
    screen.onkey(snake.go_down, "Down")

The game will start after it receive name 
from user

    name = input("Please insert name here: ")

Then the game will start. The score will start
to count when snake touch the apple icon.

        for f in foods[:6]:
        if snake.eat(f):
            f.jump()
            point.score += 10
            point.update_score()

In case the snake touch the border, player will
have 5 chances before they lose.

            elif snake.hit_boarder(border):
            snake.direction = "Stop"
            point.life -= 1
            heart = lives.pop()
            heart.jump()
            time.sleep(1)
            snake.goto(0, 0)
            if point.score >= point.high_score:
                point.high_score = point.score
                point.score_round.append(point.score)
                point.score = 0
            else:
                point.score_round.append(point.score)
                point.score = 0

The score will set back to zero everytime
the snake hits the border

After the game finished, the program will 
show all the game record which include 
player's name, high score of all time,
high score of this player, and time stamp

    record = {"name": point.name, "high score": point.high_score, 
          "high score of this round": max(point.score_round), 
          "timestamp": str(datetime.now())}
    file = open("scores.txt", "a")
    file.write(f"{record}\n")
    file = open("scores.txt", "r")
    print("Game record")
    for i in file:
        print(i)


#### Addition explanation
The reason why I put these following code
before everything else:

    try:
    file = open("scores.txt", "r")
    scores = file.read().splitlines()
    scores_list = []
    for score in scores:
        score_word = score.find("score")
        start = score.find(":", score_word)
        stop = score.find(",", start)
        highest_score = int(score[start + 2:stop])
        scores_list.append(highest_score)
    highest_score = max(scores_list)
    except FileNotFoundError:
        highest_score = 0

These set of code is for finding the highest 
score of all player to display on the screen 
from `scores.txt` as the 'High score' in the
game. If the file does not exist, in case of
the first to ever open this game, the highest
score will set to zero.