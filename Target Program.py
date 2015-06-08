#Target program that will import the turtle program and
#draw a target. Each shape in the target will be a

import turtle as t
import random as r

#a function that will take in the size, the length,
#the color and the pencolor to make a circle
def edgedCircle(size,length,color,pencolor):
    t.ht()
    t.speed(0)
    t.penup()
    t.forward(size)
    t.left(90)
    t.pendown()
    t.pencolor(pencolor)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size,360)
    t.end_fill()
    t.left(90)
    t.penup()
    t.home()
    t.left(90)
    t.pendown()
    t.st()

#a function that will take in the size and the length
#it is meant to call the edgedCircle function and will
#use the passed in size and length. The size and length will
#be passed into the edged circle functions.
def target(size,length):
    edgedCircle(size,length,"white","black")
    edgedCircle((size-length),length,"white","black")
    edgedCircle((size-length*2),length,"black","white")
    edgedCircle((size-length*3),length,"black","white")
    edgedCircle((size-length*4),length,"light blue","black")
    edgedCircle((size-length*5),length,"light blue","black")
    edgedCircle((size-length*6),length,"red","black")
    edgedCircle((size-length*7),length,"red","black")
    edgedCircle((size-length*8),length,"gold","black")
    edgedCircle((size-length*9),length,"gold","black")

#a function that will use the turtle program to draw a
#tiny dot after the target has been made. It will use
#the turlte program to also calculate where radius of
#the dot can land on.
def shoot():
    t.penup()
    t.home()
    t.speed(0)
    t.ht()
    t.shape('arrow')
    t.pencolor("grey")
    size=r.randint(0,250)
    t.forward(size)
    t.left(90)
    t.circle(size,size)
    t.st()
    t.dot(10,"purple")

#the score is going to be calculated depending on the
#distance of where the dot is from the middle of the
#target
def score():
    distance = t.distance((0,0))
    print(distance)
    if(200<distance<=250):
        return('1')
    if(175<distance<=200):
        return('2')
    if(150<distance<=170):
        return('3')
    if(125<distance<=150):
        return('4')
    if(100<distance<=125):
        return('5')
    if(75<distance<=100):
        return('6')
    if(50<distance<=75):
        return('7')
    if(25<distance<=50):
        return('8')
    if(15<distance<=25):
        return('9')
    if(0<distance<=15):
        return('10')


#uses the turtle program to display the
#score in the middle of the program
def displayScore():
    s = score()
    t.penup()
    t.home()
    t.goto((-100,-205))
    t.pendown()
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.forward(300)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(50)
    t.end_fill()
    t.penup()
    t.goto((0,-250))
    t.pendown()
    t.pencolor("black")
    t.write("Score: " +str(s),align="center",font=("arial",30))
    t.ht()
    t.penup()
    t.home()

#shoots one time and makes a target
#from the passed in integers into
#the target function.
def singleShot():
    target(200,15)
    shoot()
    displayScore()

#a reshoot function that can
#reshoot again
def reshoot():
    shoot()
    s = score()
    displayScore()

singleShot()
