"""Dragon Curve"""
import sys, turtle
Gcount = 0
wn = turtle.Screen()
turtle.hideturtle()
turtle.penup()
turtle.backward(250)
turtle.left(90)
turtle.forward(200)
turtle.right(135)
turtle.pendown()

def rRecursive(count, length):
    count -= 1
    newLength = ((length**2)/2)**0.5
    if count > 0:
        turtle.left(45)
        lRecursive(count, newLength)
        turtle.right(90)
        rRecursive(count, newLength)
        turtle.left(45)
    else:
        turtle.left(45)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.left(45)

def lRecursive(count, length):
    count -= 1
    newLength = ((length**2)/2)**0.5
    if count > 0:
        turtle.right(45)
        lRecursive(count, newLength)
        turtle.left(90)
        rRecursive(count, newLength)
        turtle.right(45)
    else:
        turtle.right(45)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.right(45)

try:
    Gcount = int(input("Psudeo Order: "))
    filename = "Order{0}PseudoDragonCurve.ps".format(Gcount)
    print(filename)
    rRecursive(Gcount, 350)
    print("Finished")
    turtle.getscreen().getcanvas().postscript(file=filename)
except ValueError:
    raise ValueError("Order must be positive interger")

sys.exit()
