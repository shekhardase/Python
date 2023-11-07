import turtle

t = turtle.Turtle()
t.speed(0)


t.penup()
t.setposition(-100, 100)
t.setheading(45)


t.pencolor("#00BFFF")
t.pensize(3)


for i in range(1111):
    t.forward(i * 10)
    t.right(110)
    t.write("Sorry", font=("Arial", 24, "bold"))

