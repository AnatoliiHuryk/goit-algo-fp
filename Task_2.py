import turtle
import math

def draw_tree(t, branch_length, angle, depth):
    if depth == 0:
        return
    else:
        t.forward(branch_length)

        position = t.position()
        heading = t.heading()

        t.left(angle)
        draw_tree(t, branch_length * math.sqrt(2) / 2, angle, depth - 1)

        t.setposition(position)
        t.setheading(heading)

        t.right(angle)
        draw_tree(t, branch_length * math.sqrt(2) / 2, angle, depth - 1)

        t.setposition(position)
        t.setheading(heading)

        t.backward(branch_length)

screen = turtle.Screen()
screen.setup(width=800, height=800)
t = turtle.Turtle()
t.speed(0)
t.left(90)


depth = int(input("Enter the depth of recursion: "))
angle = 45
initial_branch_length = 100 

draw_tree(t, initial_branch_length, angle, depth)

turtle.done()
