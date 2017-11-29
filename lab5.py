from turtle import *
import turtle
import random
colormode(255)
class square(Turtle):
    def __init__ (self,size,color,speed):
         Turtle.__init__ (self)
         self.shape("square")
         self.shapesize(size)
         self.color(color)
         self.speed(speed)
    def randomly(self):
        self.goto(random.randint(0,255),random.randint(0,255))
    

s1=square(2,"blue",6)
s1.randomly()

##class Hexagon(Turtle):
##    def __init__(self,color):
##        Turtle.__init__(self)
##        self.begin_poly()
##        for i in range(6):
##            self.penup()
##            self.forward(10)
##            self.right(60)
##        self.end_poly()
##        self.color(color)
##        register_shape("hexagon", self.get_poly())
##        self.shape("hexagon")
##
##
##shape1= Hexagon("blue")
