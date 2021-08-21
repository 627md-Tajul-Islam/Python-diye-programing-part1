import turtle
turtle.shape("circle")
turtle.speed(10)

def draw_square(lengths):
    for i in range(4):
        turtle.forward(lengths)
        turtle.left(90)

counter = 0
while counter <1:
    draw_square(100)
    turtle.right(4)
    counter = counter + 1

turtle.exitonclick()