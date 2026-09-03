from tkinter import *
import random

# ------------------
# variables globales
# ------------------
BASE = 700
ALTURA = 400
x_carro1 = 50
x_carro2 = 50
y_carro1 = 130
y_carro2 = 270

# -------------------
# funciones
# -------------------

# Funcion para dibujar la carretera
def dibujar_carretera():
    c.create_rectangle(0, 50, BASE, 350, fill="gray")

    # Linea del centro
    c.create_line(0, 200, BASE, 200, fill="white", width=3)

    # Linea de salida
    c.create_rectangle(40, 50, 50, 350, fill="yellow")

    # Meta
    c.create_rectangle(BASE - 50, 50, BASE - 20, 350, fill="white")

    # Cuadros negros de la meta
    for y in range(50, 350, 20):
        c.create_rectangle( BASE - 50, y,BASE - 30, y + 20,fill="black")


# Funcion para dibujar el carro rojo
def dibujar_carro1():
    c.create_rectangle(x_carro1,y_carro1, x_carro1 + 50,y_carro1 + 30,fill="red")

    c.create_oval( x_carro1 + 5, y_carro1 + 20, x_carro1 + 18,y_carro1 + 35,fill="black" )

    c.create_oval( x_carro1 + 32, y_carro1 + 20,x_carro1 + 45,y_carro1 + 35,fill="black" )


# Funcion para dibujar el carro azul
def dibujar_carro2():
    c.create_rectangle(  x_carro2,y_carro2,x_carro2 + 50, y_carro2 + 30, fill="blue" )

    c.create_oval( x_carro2 + 5, y_carro2 + 20, x_carro2 + 18,y_carro2 + 35,fill="black" )

    c.create_oval( x_carro2 + 32,y_carro2 + 20, x_carro2 + 45, y_carro2 + 35, fill="black")
    


# Funcion para iniciar la carrera
def iniciar_carrera():
    global x_carro1
    global x_carro2
    global velocidad1
    global velocidad2

    # Los carros vuelven al inicio
    x_carro1 = 50
    x_carro2 = 50

    # Cada carro recibe una velocidad aleatoria
    velocidad1 = random.randint(2, 8)
    velocidad2 = random.randint(2, 8)
    carrera()


# Funcion para mover los carros
def carrera():
    global x_carro1
    global x_carro2

    # Mover los carros
    x_carro1 = x_carro1 + velocidad1
    x_carro2 = x_carro2 + velocidad2

    # Borrar canvas
    c.delete("all")

    # Dibujar carretera y carros
    dibujar_carretera()
    dibujar_carro1()
    dibujar_carro2()

    # Comprobar ganador
    if x_carro1 >= BASE - 80:
        c.create_text (350, 20, text="GANO EL CARRO ROJO",fill="red",font=("Arial", 18))

    elif x_carro2 >= BASE - 80:
        c.create_text(350, 20, text="GANO EL CARRO AZUL",fill="blue",font=("Arial", 18))

    else:
        ventana_principal.after(50, carrera)


# -----------------
# ventana principal
# -----------------

ventana_principal = Tk()

ventana_principal.title("Carrera de carros")

ventana_principal.resizable(False, False)

ventana_principal.geometry("720x450")

ventana_principal.config(bg="pink")


# -----------------
# canvas
# -----------------

c = Canvas( ventana_principal, width=BASE,height=ALTURA,bg="green")

c.place(x=10, y=10)


# Dibujar escenario
dibujar_carretera()
dibujar_carro1()
dibujar_carro2()


# -----------------
# boton
# -----------------

bt_iniciar = Button(ventana_principal,text="INICIAR CARRERA",command=iniciar_carrera)

bt_iniciar.place( x=300, y=415)

# -----------------
# desplegar ventana
# -----------------

ventana_principal.mainloop()
