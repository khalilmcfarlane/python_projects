import math
import turtle

bob = turtle.Turtle()
def polygon(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
    turtle.mainloop()

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference/n
    polygon(t, n, length)

circle(bob, 20)

