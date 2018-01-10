from turtle import Turtle
import turtle
from Ball import Ball
import time
import random

turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
MY_BALL=Ball(0,0,0,0,10,"red")
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=100
MINIMUM_BALL_DX=-5
MAXIMUM_BALL_DX=5
MINIMUM_BALL_DY=-5
MAXIMUM_BALL_DY=-5
BALLS=[Ball]
for i in range (NUMBER_OF_BALLS):
    
    x_ball=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
    y_ball=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
    dx_ball=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
    dy_ball=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
    r_ball=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
    color=(random.random(), random.random(),random.random())

Ball(x_ball,y_ball,dx_ball,dy_ball,r_ball,color)
