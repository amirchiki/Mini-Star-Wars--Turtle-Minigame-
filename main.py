import turtle
import random
import math
import winsound



        # Setting up the screen
window = turtle.Screen()
window.bgcolor("white")
window.bgpic("space_background.png")
window.tracer(3)


        # creating our boarder
border = turtle.Turtle()
border.penup()
border.color("white")
border.setposition(-300, -300)
border.pendown()
border.pensize(3)

for side in range(4):
    border.forward(600)
    border.left(90)

border.hideturtle()

    # player

player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(0)


    # create our score variable
score = 0




 # create goals
maxGoals = 6
goals = []

for count in range (maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300,300), random.randint(-300,300))
    
 


  


        # set speed variable
speed = 1
def turnleft():
    player.left(10)

def turnright():
    player.right(10)

def increasespeed():
    global speed
    speed += 1
    
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False
        


turtle.listen()
turtle.onkeypress(turnleft, "a")
turtle.onkeypress(turnright, "d")
turtle.onkey(increasespeed, "w")




while True:
    player.forward(speed)

    # boundary checker
    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        winsound.PlaySound("bounce.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    # goals spawning
    for count in range(maxGoals):
        goals[count].forward(1)

        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
            

    # Collision Testing
        if isCollision(player, goals[count]):
            goals[count].setposition(random.randint(-290, 290), random.randint(-290, 290))
            goals[count].right(random.randint(0, 360))
            winsound.PlaySound("catch.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            score += 1
            print(score)


        # Draw the score on the screen
            border.undo()
            border.penup()
            border.hideturtle()
            border.setposition(-290, 310)
            scorestring = "Score: %s" %score
            border.write(scorestring, False, align="left", font=("Arial", 14, "normal"))



delay = input("Press Enter to finish")



