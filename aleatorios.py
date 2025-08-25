import turtle 
import random 
ventana = turtle.Screen()
t=turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.width(2)
t.speed(0)
turtle.colormode(255)
while True:
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    largo = random.randint(10, 100)
    angulo = random.randint(0, 100)
    t.color(color1, color2, color3)
    t.forward(largo)
    t.right(angulo)

    turtle.done
