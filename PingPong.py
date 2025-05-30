#Turtle graphics for GUI
import turtle

#Creates and returns a Singelton screen object and set all properties
screen = turtle.Screen()
screen.title("PingPong")
screen.bgcolor("Blue")
screen.setup(width=800, height=600)

screen.tracer(0)



#continuously performs a turtle screne update .
while(1):
    screen.update()
    
    
    
    