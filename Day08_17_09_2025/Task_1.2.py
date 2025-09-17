import turtle

square = turtle.Screen()
turtles = turtle.Turtle()
turtles.color("red")

for i in range(0, 4):
    turtles.forward(120)
    turtles.right(90)
square.exitonclick()
