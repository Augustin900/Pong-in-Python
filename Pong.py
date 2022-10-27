import turtle
from tkinter import *
import time

ballSpeed = 0.5
scoreA = 0
scoreB = 0
root = Tk()

root.title("Credits")
root.geometry("250x100")
labelTwo = Label(root, text="Tools Used:\n\n\n1:Visual Studio Code\n2:Scratch Online Editor").pack()
time.sleep(3)

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.addshape("C:/Users/HP/Desktop/Joc Pong in Python/ball.gif")
wn.addshape("C:/Users/HP/Desktop/Joc Pong in Python/paddle.gif")

paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("C:/Users/HP/Desktop/Joc Pong in Python/paddle.gif")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("C:/Users/HP/Desktop/Joc Pong in Python/paddle.gif")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("C:/Users/HP/Desktop/Joc Pong in Python/ball.gif")
ball.penup()
ball.goto(0, 0)
ball.dx = ballSpeed
ball.dy = ballSpeed

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")

while True:
    fps = turtle.speed()
    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
   
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
 
    if (ball.xcor() > -340 and ball.xcor() < -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40):
        ball.setx(340)
        ball.dx *= -1  