from turtle import *
colormode(255)
import turtle
from Ball import Ball
import time
import random
import math

turtle.hideturtle()
turtle.tracer(0)
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
MY_BALL=Ball(0,0,0,0,20,"red")
NUMBER_OF_BALLS=5
MINIMUM_BALL_RADIUS=10
MAXIMUM_BALL_RADIUS=50
MINIMUM_BALL_DX=-2
MAXIMUM_BALL_DX=2
MINIMUM_BALL_DY=-2
MAXIMUM_BALL_DY=2
BALLS=[]


for i in range (NUMBER_OF_BALLS):
        x_ball=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
        y_ball=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
        dx_ball=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
        dy_ball=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
        r_ball=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
        color=(random.randint(0,255), random.randint(0,255),random.randint(0,255))
        b=Ball(x_ball,y_ball,dx_ball,dy_ball,r_ball,color)
        BALLS.append(b)
        
def move_all_balls():
    for b in  BALLS:
        b.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def colide(ball,ball2):
    if ball==ball2:
        return False
    d=math.sqrt(math.pow(ball.xcor()-ball2.xcor(),2)+math.pow(ball.ycor()-ball2.ycor(),2))
    if d + 10 <=ball.r+ball2.r:
        return True
    else:
        return False
    



    
    
def check_collision():
    for ball1 in BALLS:
        for ball2 in BALLS:
            if colide(ball1,ball2):

                 x_ball=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                 y_ball=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                 dx_ball=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                 dy_ball=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                 while dx_ball == 0:
                         dx_ball =random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                 while dy_ball==0:
                         dy_ball=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                 r_ball=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                 color=(random.randint(0,255), random.randint(0,255),random.randint(0,255))
                 if ball1.r>ball2.r:
                    ball1.r += 1
                    ball1.shapesize(ball1.r/10)

                    ball2.goto(x_ball, y_ball)
                    ball2.x = x_ball
                    ball2.y= y_ball
                    ball2.dx= dx_ball
                    ball2.dy= dy_ball
                    ball2.r=r_ball
                    ball2.color=color
                    ball2.shapesize(ball2.r/10)
                 else:
                    ball2.r += 1
                    ball2.shapesize(ball2.r/10)

                    ball1.goto(x_ball, y_ball)
                    ball1.x = x_ball
                    ball1.y= y_ball
                    ball1.dx= dx_ball
                    ball1.dy= dy_ball
                    ball1.r=r_ball
                    ball1.color=color
                    

                    ball1.shapesize(ball1.r/10) 
                  

def check_myball_collision():
    for b in  BALLS:
        if colide(b,MY_BALL):
           
            if b.r>MY_BALL.r:
                return False
            else:
                MY_BALL.r+=1
                MY_BALL.shapesize(MY_BALL.r/10)
                
                x_ball=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                y_ball=random.randint(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS,SCREEN_WIDTH-MAXIMUM_BALL_RADIUS)
                dx_ball=random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                dy_ball=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                while dx_ball == 0:
                        dx_ball =random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
                while dy_ball==0:
                        dy_ball=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
                r_ball=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
                color=(random.randint(0,255), random.randint(0,255),random.randint(0,255))

                b.goto(x_ball, y_ball)
                b.x = x_ball
                b.y= y_ball
                b.dx= dx_ball
                b.dy= dy_ball
                b.r=r_ball
                b.color=color
                b.shapesize(r_ball/10)
                 
                  
    return True

        

        
def movearound(event):
    mouse_x=event.x-SCREEN_WIDTH
    mouse_y=-event.y+SCREEN_HEIGHT
    MY_BALL.goto(mouse_x, mouse_y)
    
turtle.Screen().getcanvas().bind('<Motion>',movearound)
turtle.getscreen().listen()

while RUNNING:
        if SCREEN_WIDTH!=turtle.getcanvas().winfo_width()/2  or SCREEN_HEIGHT!=turtle.getcanvas().winfo_height()/2:
                SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
                SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
        move_all_balls()
        check_collision()
        MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
        RUNNING = check_myball_collision()

        turtle.getscreen().update()
        time.sleep(SLEEP)
        
        
                
                







