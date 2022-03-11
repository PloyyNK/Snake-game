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

name = input("Please insert name here: ")

import turtle
import time
from snake import Snake
from food import Food
from border import Border
from score import Score
from datetime import datetime
from life import Life

# Create screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgpic("snake_bg.png")
screen.setup(600, 600)
screen.tracer(0)

# Create class instances
snake = Snake()
border = Border()
point = Score(name, highest_score)

# draw border
border.draw_border()

# Multiple food
foods = []
for i in range(6):
    foods.append(Food())

# create heart
lives = []
for l in range(5):
    lives.append(Life(l * -25, 270))

# keyboard binding
screen.listen()
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")

# Main loop:
delay = 0.1
while point.life > 0:
    screen.update()
    snake.move()
    time.sleep(delay)
    for f in foods[:6]:
        if snake.eat(f):
            f.jump()
            point.score += 10
            point.update_score()
        elif snake.hit_border():
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
            point.update_score()
record = {"name": point.name, "high score": point.high_score,
          "high score of this round": max(point.score_round),
          "timestamp": str(datetime.now())}
file = open("scores.txt", "a")
file.write(f"{record}\n")
file = open("scores.txt", "r")
print("---------------------------------------------")
print("Game record")
for i, ele in enumerate(file):
    print(f"{i+1}: {ele}")  # show all score of all players
    print("---------------------------------------------")
file.close()
