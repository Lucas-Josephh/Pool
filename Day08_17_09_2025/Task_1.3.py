# Ce code creer 3 cercles rouge de rayon 42 sur un fond noir

import turtle

toto = turtle.Screen()
toto.bgcolor("black")
titi = turtle.Turtle()
titi.color("red")
for i in range(3):
    titi.right(90)
    titi.circle(42)
toto.exitonclick()
