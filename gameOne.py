import turtle
import time

window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)

# Player A
playerA = turtle.Turtle()
playerA.speed(0) # move on screen
playerA.shape("square")
playerA.color("white")
playerA.shapesize(stretch_wid=5, stretch_len=1)
playerA.penup()
playerA.goto(-350, 0)

# Player B
playerB = turtle.Turtle()
playerB.speed(0) # move on screen
playerB.shape("square")
playerB.color("white")
playerB.shapesize(stretch_wid=5, stretch_len=1)
playerB.penup()
playerB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # move on screen
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# ball move 2px 
ball.dx = 2
ball.dy = 2

# Funtion move player A up
def playerAUp():
    y = playerA.ycor()
    y += 20
    playerA.sety(y)

# Funtion move player A down   
def playerADown():
    y = playerA.ycor()
    y -= 20
    playerA.sety(y)

# Funtion move player B up
def playerBUp():
    y = playerB.ycor()
    y += 20
    playerB.sety(y)

# Funtion move player B down   
def playerBDown():
    y = playerB.ycor()
    y -= 20
    playerB.sety(y)


# Keyboard binding
window.listen()
# Player A
window.onkeypress(playerAUp, "u")
window.onkeypress(playerADown, "d")

# Player B
window.onkeypress(playerBUp, "Up")
window.onkeypress(playerBDown, "Down")

def moveBalls():
    window.update()
    time.sleep(0.02)
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() > 340 and (ball.ycor() < playerB.ycor() + 40 and ball.ycor() > playerB.ycor() - 40):
        ball.dx *= -1
    window.ontimer(moveBalls(), 100)


moveBalls()
