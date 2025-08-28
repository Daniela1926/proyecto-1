import turtle 
ventana = turtle.Screen()
t=turtle.Turtle()
t.color ("blue")

for i in range (8):
    t.circle (100)
    t.left(45)

t.write("flor", font=("arial", 30, "normal"))
turtle.done()