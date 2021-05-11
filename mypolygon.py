import turtle
# Creates a square using turtle interface
# NOTE: RT/LT deals with angles, FD and BK deal with distance
bob = turtle.Turtle()
print(bob)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.rt(90)
bob.bk(100)
bob.lt(90)
bob.bk(100)
turtle.mainloop()
