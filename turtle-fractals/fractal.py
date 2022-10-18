"""Koch Snoflake"""
import turtle
count = 0
wn = turtle.Screen()
turtle.hideturtle()
turtle.penup()
turtle.backward(400)
turtle.pendown()

def drawseed(length):
    len = length/3
    turtle.forward(len)
    turtle.left(60)
    turtle.forward(len)
    turtle.right(120)
    turtle.forward(len)
    turtle.left(60)
    turtle.forward(len)

def recursive(count, length):
    count -= 1
    len = length/3
    if count>1:
        recursive(count,len)
        turtle.left(60)
        recursive(count,len)
        turtle.right(120)
        recursive(count,len)
        turtle.left(60)
        recursive(count,len)
    else:
        drawseed(len)

try:
    count = int(input("Psudeo Order: "))
    recursive(count, 2400)
    print("Finished")
except ValueError:
    raise ValueError("Order must be positive interger")
