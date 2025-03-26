import turtle

turtle.Screen().bgcolor("blue")

x = turtle.Screen()
x.setup(400,300)

turtle.title("the world of the blue square")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)
    i= i+1