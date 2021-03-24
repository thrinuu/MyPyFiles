import turtle

#Inidan Flag Circle

flag = turtle.Turtle()
flag.color("black")
flag.speed(100)
flag.begin_fill()

for i in range(24):
	flag.forward(50)

	flag.penup()
	flag.setposition(0, 0)
	flag.pendown()
	flag.right(15)
flag.setposition(0, -50)
flag.circle(50)
flag.penup()
#For Applied color to the top
flag.setposition(-500, 100)
flag.pendown()
flag.fillcolor('#fc480a')
flag.begin_fill()
flag.forward(1000)
flag.left(90)
flag.forward(300)
flag.left(90)
flag.forward(1000)
flag.left(90)
flag.forward(300)
flag.end_fill()
flag.penup()
#Secondary Applied color to the down 
flag.setposition(-500, -100)
flag.pendown()
flag.fillcolor('#29a329')
flag.begin_fill()
flag.right(270)
flag.forward(1000)
flag.right(90)
flag.forward(300)
flag.right(90)
flag.forward(1000)
flag.right(90)
flag.forward(300)
flag.end_fill()
flag.penup()

turtle.done()
