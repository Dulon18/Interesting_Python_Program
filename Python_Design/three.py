import turtle

color=('red','green','yellow','blue','orange','white')

t=turtle.Turtle()
s= turtle.Screen()
s.bgcolor('black')
t.speed(25)

for i in range(150):
    t.color(color[i % 6])
    t.forward( i*4 )
    t.left(160)
    t.width(2)
