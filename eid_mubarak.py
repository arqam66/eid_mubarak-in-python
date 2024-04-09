
#import packages
from turtle import *
from random import randint
import math, os, time

#initialzie and setup
myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = Screen()
window.title("Eid Mubarak !!")
window.screensize(300, 300)
window.bgcolor("#072752")


#Methods
def draw_circle(paint, color, x, y, radius):
  paint.penup()
  paint.color(color)
  paint.fillcolor(color)
  paint.goto(x,y)
  paint.pendown()
  paint.begin_fill()
  paint.circle(radius)
  paint.end_fill()

def draw_star(paint, color, x, y, size):
  paint.penup()
  paint.color(color)
  paint.fillcolor(color)
  paint.goto(x,y)
  paint.pendown()
  paint.begin_fill()
  paint.right(144)
  for i in range(5):
    paint.forward(size)
    paint.right(144)
    paint.forward(size)
  paint.end_fill()
  paint.setheading(0)


def draw_rectangle(paint, color, x, y, width, height):
  paint.penup()
  paint.color(color)
  paint.fillcolor(color)
  paint.goto(x,y)
  paint.pendown()
  paint.begin_fill()
  for i in range (2):
    paint.forward(width)
    paint.left(90)
    paint.forward(height)
    paint.left(90)
    
  paint.end_fill()
  paint.setheading(0)


def draw_trapizium(paint, color, x, y, width, height, style):
  rad = 20*(math.pi/180) #angle in radian for calculating parallel side  
  paint.penup()
  paint.color(color)
  paint.fillcolor(color)
  paint.goto(x,y)
  paint.pendown()
  paint.begin_fill()

  if(style == "normal"):
    nor = 1
    rev = 0
  elif(style == "reverse"):
    nor = 0
    rev = 1

  paint.forward(width - rev * (2 * height * math.sin(rad))) # parallel side
  paint.left(90 + (20 * nor) - (20 * rev))
  paint.forward(height)
  paint.left(90 - (20 * nor) + (20 * rev))
  paint.forward(width - nor * (2 * height * math.sin(rad))) # parallel side
  paint.left(90 - (20 * nor) + (20 * rev))
  paint.forward(height)
  paint.left(110 + (20 * nor) - (20 * rev))
  
  paint.end_fill()
  paint.setheading(0) 


#draw masjid and minar
def draw_minar(paint, color, x, y):
  paint.penup()
  paint.color(color)
  paint.fillcolor(color)
  paint.goto(x,y)
  paint.pendown()
  paint.begin_fill()

  #first turn
  paint.forward(60)
  paint.left(90)
  paint.forward(40)
  paint.left(45)
  paint.forward(35)
  paint.right(45)
  paint.forward(30)
  paint.left(45)
  paint.forward(7.42) #from pythagorean theorem

  
  #second turn
  paint.left(90)
  paint.forward(7.42) #from pythagorean theorem
  paint.left(45)
  paint.forward(30)
  paint.right(45)
  paint.forward(35)
  paint.left(45)
  paint.forward(40)
  
  paint.end_fill()
  paint.setheading(0)


  
################### Logic #####################  
#Now draw the masjid
draw_rectangle(myPen, "#ffdf00", 250, -280, 50, 8)
draw_trapizium(myPen, "white",  245, -265, 60, 12, "normal")

draw_rectangle(myPen, "#ffa500", 250, -245, 10, 70) 
draw_rectangle(myPen, "#ffc500", 267, -245, 16, 70) 
draw_rectangle(myPen, "#ffa500", 290, -245, 10, 70)

draw_trapizium(myPen, "white",  250, -168, 60, 12, "reverse")

draw_rectangle(myPen, "white", 233, -145, 10, 20) 
draw_rectangle(myPen, "white", 245, -145, 60, 20) 
draw_rectangle(myPen, "white", 307, -145, 10, 20)

draw_trapizium(myPen, "#ffa500", 238, -115, 75, 18, "normal")
draw_rectangle(myPen, "#ffdf00",245, -90, 60, 15)

draw_minar(myPen, "#6799ff", 245, -65)

#Let's draw the moon
draw_circle(myPen, "white", 210, -10, 30)
draw_circle(myPen, "#072752", 203, -3, 30)

#Now draw the stars
draw_star(myPen, "white", 280, 70, 13)
for i in range (1, 18):
  x = randint(-220, 215)
  y = randint(-75, 270)
  size = randint(8,15)
  draw_star(myPen, "white", x, y, size)



# time for text printing 
myPen.penup()
myPen.setposition(-85, -140)
image_name = "./images/cow.gif"
# add the shape first then set the turtle shape
window.addshape(os.path.join(os.path.dirname(__file__), image_name))
myPen.shape(os.path.join(os.path.dirname(__file__), image_name))
myPen.stamp()

myPen.color("white")
myPen.goto(-80, -240)
myPen.write("Eid Mubarak", False, "center", ("Gabriola",38, ("bold","italic")))
myPen.goto(-350, -260)
myPen.write("May the blessing of Allah fill your life with happiness and success", False, "left", "9pt")

myPen.goto(-230, -320)
myPen.write("@Presented By: Arqam Hussain", False, "left", ("0.5pt"))

myPen.penup()
myPen.goto(600, 600)
window.exitonclick()