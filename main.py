import random
import time
import os
import turtle

# Global variables
d = 13
score = 0
high_score = 0
code_running = "true"
delay = 0.01

# Screen
wn = turtle.Screen()
wn.bgcolor("#a6fbff")
wn.setup(width=450, height=800)
wn.tracer(0)
# wn.register_shape("/Users/sarthakchauhan/PycharmProjects/game/venv/images/flappy_bird.gif")
wn.register_shape("./venv/images/bird.gif")

# Pillars
pillar_up = turtle.Turtle()
pillar_up.shape("square")
pillar_up.color("green")
pillar_up.shapesize(stretch_len=4, stretch_wid=40)
pillar_up.penup()
pillar_up.goto(100, 500)
pillar_up.speed(0)


pillar_down = turtle.Turtle()
pillar_down.shape("square")
pillar_down.color("green")
pillar_down.shapesize(stretch_len=4, stretch_wid=40)
pillar_down.penup()
pillar_down.goto(100, -500)
pillar_down.speed(0)

# Openings
pillar_up_opening = turtle.Turtle()
pillar_up_opening.shape("square")
pillar_up_opening.color("green")
pillar_up_opening.shapesize(stretch_len=5, stretch_wid=1)
pillar_up_opening.penup()
pillar_up_opening.goto(100, 110)
pillar_up_opening.speed(0)

pillar_down_opening = turtle.Turtle()
pillar_down_opening.shape("square")
pillar_down_opening.color("green")
pillar_down_opening.shapesize(stretch_len=5, stretch_wid=1)
pillar_down_opening.penup()
pillar_down_opening.goto(100, -110)
pillar_down_opening.speed(0)

# Bird
bird = turtle.Turtle()
bird.shape("./venv/images/bird.gif")
bird.color("yellow")
bird.speed(0)
bird.shapesize(stretch_len=3, stretch_wid=3)
bird.penup()
bird.goto(-100, 0)

# Pen
pen = turtle.Turtle()
pen.shape("square")
pen.hideturtle()
pen.penup()
pen.color("white")
pen.speed(0)
pen.goto(0, 250)
pen.write(score, align="center", font=("Courier", 72, "normal"))


# Functions
def jump():
    global d
    if bird.ycor() >= -500:
        bird.sety(bird.ycor() + d)
        d -= 1


def reset_d_for_jump():
    if code_running == "true":
        os.system("afplay ./venv/sounds/jump.wav&")
        global d
        d = 13


def reset_settings():
    global d, code_running, score
    os.system("afplay ./venv/sounds/beep-10.m4a&")
    code_running = "false"
    d = 15
    pen.goto(0, 0)
    pen.clear()
    pen.write("GAME OVER!!!\n", align="center", font=("Courier", 32, "normal"))
    pen.sety(pen.ycor() - 32)
    pen.write("\nScore:{} High Score:{}\n".format(score, high_score), align="center", font=("Courier", 32, "normal"))
    pen.write("\nPress Enter to continue", align="center", font=("Courier", 20, "normal"))
    score = 0


def reset_code_running():
    global code_running, d
    if code_running == "false":
        d = 13
        pillar_up.goto(100, 500)
        pillar_down.goto(100, -500)
        bird.goto(-125, 0)
        pillar_up_opening.goto(100, 110)
        pillar_down_opening.goto(100, -110)
        pen.goto(0, 250)
        pen.clear()
        pen.write(score, align="center", font=("Courier", 72, "normal"))
        code_running = "true"


# Keyboard Bindings
wn.listen()
wn.onkeypress(reset_d_for_jump, "space")
wn.onkeypress(reset_code_running, "Return")


while True:
    if code_running == "true":
        # movement of poles
        pillar_up.setx((pillar_up.xcor() - 3))
        pillar_down.setx((pillar_down.xcor() - 3))
        pillar_up_opening.setx((pillar_up_opening.xcor() - 3))
        pillar_down_opening.setx((pillar_down_opening.xcor() - 3))

    if pillar_up.xcor() <= -260:
        pillar_up.setx(260)
        pillar_down.setx(260)
        pillar_up_opening.setx(260)
        pillar_down_opening.setx(260)

        # Random pillars
        pillar_up.sety(random.randint(250, 750))
        pillar_down.sety(pillar_up.ycor() - 1000)
        pillar_up_opening.sety(pillar_up.ycor() - 390)
        pillar_down_opening.sety(pillar_up.ycor() - 590)

    # Incrementing Score
    if (pillar_up.xcor() == -131 or pillar_up.xcor() == -130) and code_running == "true":
        score += 1
        if high_score < score:
            high_score = score
        pillar_up.setx(pillar_up.xcor() - 1)
        pillar_down.setx(pillar_down.xcor() - 1)
        pen.clear()
        pen.write(score, align="center", font=("Courier", 72, "normal"))

    # Check for collision
    # with pipes
    if -65 >= pillar_up.xcor() >= -170 and bird.distance(pillar_up) < 420 and code_running == "true":
        reset_settings()

    if -65 >= pillar_down.xcor() >= -170 and bird.distance(pillar_down) < 420 and code_running == "true":
        reset_settings()

    if (bird.ycor() < -400 or bird.ycor() > 400) and code_running == "true":
        reset_settings()
    jump()
    time.sleep(delay)
    wn.update()
