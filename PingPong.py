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


#continuously performs a turtle screen update .
while(1):
    screen.update()
    
    
    
    