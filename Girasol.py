import math
import turtle

# Configuración inicial
turtle.bgcolor("black")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")

# Dibuja el tallo
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.setheading(90)
turtle.fillcolor("green")  # Cambia el color del tallo a verde
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

# Cambia el color del centro del girasol a café más claro (RGB: 139, 69, 19)
turtle.penup()
turtle.goto(0, -180)
turtle.fillcolor("#8B4513")  # Café más claro
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

# Código del girasol (el que proporcionaste)
phi = 137.508 * (math.pi / 180.0)
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.right(20)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.left(140)
        turtle.forward(70)
        turtle.left(40)
        turtle.forward(70)
        turtle.end_fill()

# Escribe "Te Quiero" en la parte superior del girasol
turtle.penup()
turtle.goto(0, 100)  # Ajusta la posición vertical según sea necesario
turtle.color("Red")  # Color del texto
turtle.write("Te Quiero", align="center", font=("Arial", 24, "bold"))

# Oculta el cursor de la tortuga antes de salir
turtle.hideturtle()

# Cierra la ventana al hacer clic
turtle.exitonclick()
