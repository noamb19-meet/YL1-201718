from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball=Ball(8,"red",10)
ball2=Ball(4,"blue",5)

def check_collision(ball,ball2):
    if math.sqrt(math.pow(ball.xcor()-ball2.xcor(),2)+math.pow(ball.ycor()-ball2.ycor(),2))<=ball.radius+ball2.radius:
        print("they are in collision")

    else:
        print("they are not in collision")
        



check_collision(ball,ball2)
