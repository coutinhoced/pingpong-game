#Turtle graphics for GUI
import turtle

#Creates and returns a Singelton screen object and set all properties
screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("Blue")
screen.setup(width=800, height=600)

screen.tracer(0)

#a Turtle screen object to create any shape, here we create it in far left
paddle_1 = turtle.Turtle()
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
#position based on screen co-ordinate system, with 0 being at dead center of screen
#goto will drawn a path on the canva
#we remove this line by using penup
paddle_1.penup()
paddle_1.goto(-350, 0)


#a Turtle screen object to create any shape, here we create it in far right
paddle_2 = turtle.Turtle()
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)


ball = turtle.Turtle()
ball.shape("circle")
ball.color("Red")
ball.penup()
ball.goto(0,0)
# dx and dy represents how much units the ball moves to x and y co-ordinates
ball.dx = 0.07
ball.dy = -0.07

step = 10

def moveBall():
    #the value for x and y are assigned with the steps of dx and dy
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    x =ball.xcor()
    y =ball.ycor()

    if x > 390:
        ball.setx(390)
        ball.dx = ball.dx * -1
    
    if x < -390:
        ball.setx(-390)
        ball.dx = ball.dx * -1
    
    if y > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    
    if y < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1







#Funcion to move the paddle1 up
def paddle_1_up():
    #retrieve y co-ordinate value 
    y= paddle_1.ycor()
    y = y+step
    #moving the paddle up by y units
    paddle_1.sety(y)
    # if paddle reaches the edge of screen, stop further movement
    if y > 245:
        paddle_1.sety(245)

#Funcion to move the paddle1 down
def paddle_1_down():    
    y= paddle_1.ycor()
    y = y-step    
    paddle_1.sety(y)     
    if y < -245:
        paddle_1.sety(-245)

def paddle_1_right():
    x = paddle_1.xcor()
    x = x+step
    paddle_1.setx(x)
    if x > -10:
        paddle_1.setx(-10)

def paddle_1_left():
    x = paddle_1.xcor()
    x = x-step
    paddle_1.setx(x)
    if x < -350:
        paddle_1.setx(-350)

#Funcion to move the paddle2 up
def paddle_2_up():
    #retrieve y co-ordinate value 
    y= paddle_2.ycor()
    y = y+step
    #moving the paddle up by y units
    paddle_2.sety(y)
    # if paddle reaches the edge of screen, stop further movement
    if y > 245:
        paddle_2.sety(245)

#Funcion to move the paddle2 down
def paddle_2_down():    
    y= paddle_2.ycor()
    y = y-step   
    paddle_2.sety(y)    
    if y < -245:
        paddle_2.sety(-245)

def paddle_2_right():
    x = paddle_2.xcor()
    x = x+step
    paddle_2.setx(x)
    if x > 350:
        paddle_2.setx(350)

def paddle_2_left():
    x = paddle_2.xcor()
    x = x-step
    paddle_2.setx(x)
    if x < 10:
        paddle_2.setx(10)





#event to listen to key press
screen.listen()
#Call paddle_1_up function on press of W key to move the paddle up
# Assign multiple keys to the same function
upKeys = ["w", "W"]
for key in upKeys:
    screen.onkeypress(paddle_1_up, key)

screen.onkeypress(paddle_2_up, "Up")

downKeys = ["s", "S"]
for key in downKeys:
    screen.onkeypress(paddle_1_down, key)

screen.onkeypress(paddle_2_down, "Down")


leftKeys =["a", "A"]
for key in leftKeys:
    screen.onkeypress(paddle_1_left, key)

screen.onkeypress(paddle_2_left, "Left")


rightKeys =["d", "D"]
for key in rightKeys:
    screen.onkeypress(paddle_1_right, key)

screen.onkeypress(paddle_2_right, "Right")


#continuously performs a turtle screen update .
while(1):
    screen.update()
    #call ball movement continuously
    moveBall()
    
    
    
    