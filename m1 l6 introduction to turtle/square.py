import turtle

screen=turtle.Screen()
screen.bgcolor("red")
screen.title("turtle graphics")
board=turtle.Turtle()
board.speed("fastest")
board.hideturtle()
turtle.exitonclick()
colors=["red","orange","green","blue"]
for i in range(0,4):
    board.color(colors[i%len(colors)])
    board.width(2)
    board.forward(100)
    board.left(90)
    board.forward(100)
    board.left(90)
    