"""Sierpinksi Triangle"""
import sys, turtle
Gcount = 0
wn = turtle.Screen()
turtle.hideturtle()
turtle.penup()
turtle.backward(350)
turtle.left(90)
turtle.backward(300)
turtle.right(30)
turtle.pendown()

def seed(sideLength):
    for i in range(3):
        turtle.forward(sideLength)
        turtle.right(120)

def recursive(count,sideLength):
    count -= 1
    if count > 0:
        recursive(count,sideLength/2)
        turtle.forward(sideLength/2)
        recursive(count,sideLength/2)
        turtle.right(120)
        turtle.forward(sideLength/2)
        turtle.left(120)
        recursive(count,sideLength/2)
        turtle.left(120)
        turtle.forward(sideLength/2)
        turtle.right(120)
    else:
        seed(sideLength)

try:
    Gcount = int(input("Psudeo Order: "))
    filename = "Order{0}PseudoSierpinskiTriangle.ps".format(Gcount)
    print(filename)
    recursive(Gcount, 700)
    print("Finished")
    turtle.getscreen().getcanvas().postscript(file=filename)
except ValueError:
    raise ValueError("Order must be positive interger")

sys.exit()
