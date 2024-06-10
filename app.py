import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear la tortuga para dibujar el corazón
heart = turtle.Turtle()
heart.color("red")
heart.pensize(3)
heart.speed(3)

# Función para dibujar una mitad del corazón
def draw_half_heart():
    heart.begin_fill()
    heart.left(50)
    heart.forward(133)
    heart.circle(50, 200)
    heart.right(140)
    heart.circle(50, 200)
    heart.forward(133)
    heart.end_fill()

# Dibujar la primera mitad del corazón
heart.penup()
heart.goto(-70, 0)
heart.pendown()
draw_half_heart()

# Configurar la tortuga para dibujar la línea de ruptura
heart.color("black")
heart.pensize(5)
heart.penup()
heart.goto(-70, 50)
heart.pendown()
heart.right(60)
heart.forward(100)
heart.right(120)
heart.forward(50)
heart.left(120)
heart.forward(50)
heart.right(120)
heart.forward(50)

# Ocultar la tortuga y mostrar la ventana
heart.hideturtle()
screen.mainloop()
