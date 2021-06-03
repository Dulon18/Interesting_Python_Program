#pip install turtle
import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)


while(True):
    for i in range(6):
        for colors in ['green', 'orange']:
            turtle.color(colors)
            turtle.circle(100)
            turtle.left(4)

turtle.hideturtle()
turtle.mainloop()
