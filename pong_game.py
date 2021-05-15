import time
import turtle
import winsound


speed = 5
count_s = 1
colors = ["grey", "light blue", "blue", "dark blue", "light green", "green", "dark green", "yellow", "orange", "red"]

# Draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Draw paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Draw paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Draw ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Setting the ball speed
ball.dx = speed
ball.dy = speed

# Score
score_1 = 0
score_2 = 0

# Head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 0)
hud.write("PRESS k TO START", align="center", font=("Press Start 2P", 24, "normal"))


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    paddle_2.sety(y)


# Keyboard
screen.listen()
screen.onkeypress(paddle_1_up, "w")
screen.onkeypress(paddle_1_down, "s")
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")


def victory():
    if score_1 > score_2:
        player = 1
    else:
        player = 2

    screen.update()

    if score_1 != score_2:
        hud.goto(0, 145)
        hud.write("VICTORY", align="center", font=("Press Start 2P", 24, "normal"))
        hud.goto(0, 115)
        hud.write("PLAYER {} WINS!".format(player), align="center", font=("Press Start 2P", 16, "normal"))
    else:
        hud.goto(0, 120)
        hud.write("DRAW!".format(player), align="center", font=("Press Start 2P", 36, "normal"))

    hud.goto(0, -270)
    hud.write("PRESS k TO RESTART OR y TO FINISH", align="center", font=("Press Start 2P", 12, "normal"))

    # Restarting the game
    screen.listen()
    screen.onkeypress(screen_update, "k")
    turtle.done()


def screen_update():
    global score_1
    global score_2
    global count_s

    score_1 = 0
    score_2 = 0
    count_s = 1

    ball.goto(0, 0)
    paddle_1.goto(-350, 0)
    paddle_2.goto(350, 0)

    hud.clear()
    hud.goto(0, 255)
    hud.write("P1 0 : 0 P2", align="center", font=("Press Start 2P", 24, "normal"))
    hud.goto(0, 225)
    hud.write("SPEED x1", align="center", font=("Press Start 2P", 16, "normal"))
    hud.goto(0, -270)
    hud.write("PRESS k TO RESTART OR y TO FINISH", align="center", font=("Press Start 2P", 12, "normal"))

    screen.listen()
    screen.onkeypress(victory, "y")

    while True:
        screen.update()

        # Setting ball acceleration
        time.sleep(1/60)

        # Ball movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Collision with the upper wall
        if ball.ycor() > 290:
            # Setting the sound to Windows
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.sety(290)
            ball.dy *= -1

        # Collision with lower wall
        if ball.ycor() < -290:
            # Setting the sound to Windows
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            ball.sety(-290)
            ball.dy *= -1

        # Collision with left wall
        if ball.xcor() < -390:
            score_2 += 1
            count_s = 1

            ball.color(colors[count_s - 1])

            hud.clear()
            hud.goto(0, 255)
            hud.write("P1 {} : {} P2".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
            hud.goto(0, 225)
            hud.write("SPEED x%d" % count_s, align="center", font=("Press Start 2P", 16, "normal"))
            hud.goto(0, -270)
            hud.write("PRESS k TO RESTART OR y TO FINISH", align="center", font=("Press Start 2P", 12, "normal"))

            # Setting the sound to Windows
            winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)

            ball.goto(0, 0)
            ball.dx = speed
            ball.dy = speed
            ball.dx *= -1

        # Collision with right wall
        if ball.xcor() > 390:
            score_1 += 1
            count_s = 1

            ball.color(colors[count_s - 1])

            hud.clear()
            hud.goto(0, 255)
            hud.write("P1 {} : {} P2".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
            hud.goto(0, 225)
            hud.write("SPEED x%d" % count_s, align="center", font=("Press Start 2P", 16, "normal"))
            hud.goto(0, -270)
            hud.write("PRESS k TO RESTART OR y TO FINISH", align="center", font=("Press Start 2P", 12, "normal"))

            # Setting the sound to Windows
            winsound.PlaySound("258020__kodack__arcade-bleep-sound.wav", winsound.SND_ASYNC)

            ball.goto(0, 0)
            ball.dx = speed
            ball.dy = speed
            ball.dx *= 1

        # Fixing the bug
        # Collision with the paddle 1
        if (-330 > ball.xcor() > -340) and (paddle_1.ycor() + 80 > ball.ycor() > paddle_1.ycor() - 80):
            # Changing the ball speed
            if (paddle_1.ycor() + 80 > ball.ycor() > paddle_1.ycor() + 20) or (
                    paddle_1.ycor() - 20 > ball.ycor() > paddle_1.ycor() - 80):
                ball.setx(-330)
                ball.dx *= -1

                if ball.dx < 9.5:
                    count_s += 1

                    ball.color(colors[count_s - 1])

                    hud.clear()
                    hud.goto(0, 255)
                    hud.write("P1 {} : {} P2".format(score_1, score_2), align="center",
                              font=("Press Start 2P", 24, "normal"))
                    hud.goto(0, 225)
                    hud.write("SPEED x%d" % count_s, align="center", font=("Press Start 2P", 16, "normal"))
                    hud.goto(0, -270)
                    hud.write("PRESS k TO RESTART OR y TO FINISH", align="center",
                              font=("Press Start 2P", 12, "normal"))

                    ball.dx = (ball.dx + 0.5)
                    print(ball.dx)

                # Setting the sound to Windows
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            else:
                ball.setx(-330)
                ball.dx *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        # Collision with the paddle 2
        if (330 < ball.xcor() < 340) and (paddle_2.ycor() + 80 > ball.ycor() > paddle_2.ycor() - 80):
            # Changing the ball speed
            if (paddle_2.ycor() + 80 > ball.ycor() > paddle_2.ycor() + 20) or (
                    paddle_2.ycor() - 20 > ball.ycor() > paddle_2.ycor() - 80):
                ball.setx(330)
                ball.dx *= -1

                if ball.dx > -9.5:
                    count_s += 1

                    ball.color(colors[count_s - 1])

                    hud.clear()
                    hud.goto(0, 255)
                    hud.write("P1 {} : {} P2".format(score_1, score_2), align="center",
                              font=("Press Start 2P", 24, "normal"))
                    hud.goto(0, 225)
                    hud.write("SPEED x%d" % count_s, align="center", font=("Press Start 2P", 16, "normal"))
                    hud.goto(0, -270)
                    hud.write("PRESS k TO RESTART OR y TO FINISH", align="center",
                              font=("Press Start 2P", 12, "normal"))

                    ball.dx = (ball.dx - 0.5)
                    print(ball.dx)

                # Setting the sound to Windows
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

            else:
                ball.setx(330)
                ball.dx *= -1
                winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


# keyboard
screen.listen()
# Starting the game
screen.onkeypress(screen_update, "k")
turtle.done()
