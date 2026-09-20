

import turtle
screen = turtle.Screen()
screen.bgcolor("navy blue")
screen.title("Colour Loop Artwork")
artist = turtle.Turtle()
artist.speed("fastest")
artist.hideturtle()
artist.pensize(3)
def draw_petal(size, colour):
    artist.color(colour)
    artist.begin_fill()

    for _ in range(2):
        artist.circle(size,55)
        artist.left(120)
        
    artist.end_fill()
colours = ["red", "cyan", "blue", "magenta"]
for i in range(36):
    draw_petal(90, colours[i % len(colours)])
    artist.right(10)
artist.penup()
artist.goto(0, -25)
artist.pendown()
artist.color("white")
artist.begin_fill()
artist.circle(30)
artist.end_fill()
turtle.done()