import turtle


def draw_polygone(sides):

    turtle.Screen()
    draw = turtle.Turtle()

    for i in range(sides):
        draw.forward(100)
        draw.left(360 / sides)

    turtle.exitonclick()


draw_polygone(9)
