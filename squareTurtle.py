import turtle
turtle.shape("turtle")
turtle.speed(1)

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)