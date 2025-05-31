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

#Funcion to move the paddle1 up
def paddle_1_up():
    #retrieve y co-ordinate value 
    y= paddle_1.ycor()
    y = y+10
    #moving the paddle up by y units
    paddle_1.sety(y)
    # if paddle reaches the edge of screen, stop further movement
    if y > 245:
        paddle_1.sety(245)

#Funcion to move the paddle2 up
def paddle_2_up():
    #retrieve y co-ordinate value 
    y= paddle_2.ycor()
    y = y+10
    #moving the paddle up by y units
    paddle_2.sety(y)
    # if paddle reaches the edge of screen, stop further movement
    if y > 245:
        paddle_2.sety(245)


#event to listen to key press
screen.listen()
#Call paddle_1_up function on press of W key to move the paddle up
# Assign multiple keys to the same function
upKeys = ["w", "W"]
for key in upKeys:
    screen.onkeypress(paddle_1_up, key)

screen.onkeypress(paddle_2_up, "Up")





#continuously performs a turtle screen update .
while(1):
    screen.update()
    
    
    
    