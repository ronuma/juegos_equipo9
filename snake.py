"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""
#ian luis Vazquez Moran
from turtle import *
import random
import time
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
i=0
#Ian Luis Vázquez Morán
# Rodrigo agrega los colores que pueden tener el snake y la comida
colours = ['indigo', 'lime', 'turquoise', 'black', 'orange' ]
snakeColour = colours[random.randint(0,4)]
foodColour = colours[random.randint(0,4)]
while (snakeColour == foodColour):
    snakeColour = colours[random.randint(0,4)]

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    global i
    head = snake[-1].copy()
    head.move(aim)
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        i=0
        print('Snake:', len(snake))
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
    else:
        snake.pop(0)
    if (head != food and i==40):
        food.x = random.randrange(-15, 15) * 10
        food.y = random.randrange(-15, 15) * 10
        i=0
    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColour)
    i+=1
    square(food.x,food.y, 9, foodColour)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
