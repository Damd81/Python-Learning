# Pong

import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("Green")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
player_one_score = 0
player_two_score = 0

# Paddle one
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("blue")
paddle_one.shapesize(stretch_wid=5, stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350, 0)

# Paddle two
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("red")
paddle_two.shapesize(stretch_wid=5, stretch_len=1)
paddle_two.penup()
paddle_two.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1.5)
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.shapesize(stretch_wid=1.5)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player One: 0  Player Two", align="center", font=("Courier", 24, "normal"))


# Game Function for paddles
def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)

# Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_one_up, "w")
wn.onkeypress(paddle_one_down, "s")
wn.onkeypress(paddle_two_up, "Up")
wn.onkeypress(paddle_two_down, "Down")

# Main Game Loop, runs continuously during gameplay
while True:
    wn.update()

    # Ball location
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Game border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay pong.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay pong.wav&")

    # sides
    if ball.xcor() > 350:
        player_one_score += 1
        pen.clear()
        pen.write("Player One: {} Player Two: {}".format(player_one_score, player_two_score), align="center",font=("Courier", 24))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        player_two_score += 1
        pen.clear()
        pen.write("Player One: {} Player Two: {}".format(player_one_score, player_two_score), align="center",font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_one.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50:
        ball.dx *= -1
        os.system("afplay pong.wav&")

    elif ball.xcor() > 340 and ball.ycor() < paddle_two.ycor() + 50 and ball.ycor() > paddle_two.ycor() - 50:
        ball.dx *= -1
        os.system("afplay pong.wav&")

