"""Hilbert Curve"""
# N.B. This is a bit of a crude version as I couldn't find my old implementation
from calendar import leapdays
import turtle
count = 0
wn = turtle.Screen()
turtle.screensize(700,700)
turtle.hideturtle()
turtle.penup()
turtle.backward(300)
turtle.left(90)
turtle.backward(300)
turtle.pendown()

def segments(count):
    if(count > 1):
        return 2*segments(count-1) +1
    else:
        return 3

def seedL(length):
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)

def seedR(length):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)

def recursiveR(count, length):
    count -= 1
    rec = length/segments(count)
    rec_ = segments(count-1)*rec
    len = length/3
    if count>1:
        turtle.right(90)
        recursiveL(count,rec_)
        turtle.right(90)
        turtle.forward(rec)
        recursiveR(count,rec_)
        turtle.left(90)
        turtle.forward(rec)
        turtle.left(90)
        recursiveR(count,rec_)
        turtle.forward(rec)
        turtle.right(90)
        recursiveL(count,rec_)
        turtle.right(90)
    else:
        turtle.right(90)
        seedL(len)
        turtle.right(90)
        turtle.forward(len)
        seedR(len)
        turtle.left(90)
        turtle.forward(len)
        turtle.left(90)
        seedR(len)
        turtle.forward(len)
        turtle.right(90)
        seedL(len)
        turtle.right(90)

def recursiveL(count, length):
    count -= 1
    rec = length/segments(count)
    rec_ = segments(count-1)*rec
    len = length/3
    if count>1:
        turtle.left(90)
        recursiveR(count,rec_)
        turtle.left(90)
        turtle.forward(rec)
        recursiveL(count,rec_)
        turtle.right(90)
        turtle.forward(rec)
        turtle.right(90)
        recursiveL(count,rec_)
        turtle.forward(rec)
        turtle.left(90)
        recursiveR(count,rec_)
        turtle.left(90)
    else:
        turtle.left(90)
        seedR(len)
        turtle.left(90)
        turtle.forward(len)
        seedL(len)
        turtle.right(90)
        turtle.forward(len)
        turtle.right(90)
        seedL(len)
        turtle.forward(len)
        turtle.left(90)
        seedR(len)
        turtle.left(90)

try:
    count = int(input("Psudeo Order: "))
    recursiveR(count, 600)
    print("Finished")
except ValueError:
    raise ValueError("Order must be positive interger")
