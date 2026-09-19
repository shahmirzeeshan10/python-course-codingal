import turtle
screen=turtle.Screen()
screen.bgcolor("white")
screen.title("neon mandela")
pen1=turtle.Turtle()
pen1.speed("fastest")
colors=["green","red","black","grey"]
for i in range(90):
    pen1.color(colors[i %len(colors)])
    pen1.width(9)
    pen1.forward(i*8)
    pen1.right(90)

pen1.penup()
pen1.goto(0,-60)
pen1.setheading(90)
pen1.pendown()
pen1.color("gold","silver")
pen1.begin_fill()
for i in range(5):
    pen1.forward(135)
    pen1.right(144)
pen1.end_fill()
turtle.done()