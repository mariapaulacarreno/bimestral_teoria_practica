from tkinter import *
import random

# ------------------
# variables globales
# ------------------
BASE = 760
ALTURA = 360
x1 = 10
x2 = 10
hay_ganador = False  

# -------------------
# funciones
# -------------------


def iniciar_carrera():
    b_i.config(state="disabled")
    mover_carro_1()
    mover_carro_2()

def mover_carro_1(event=None):
    global x1, carro_1, hay_ganador, img_carro_1

    if 'carro_1' not in globals():
        img_carro_1 = PhotoImage(file="img/carro_rojo.png")
        carro_1 = c.create_image(x1, 40, image=img_carro_1, anchor=NW)
        
    x1 += random.randint(1, 10)
    c.coords(carro_1, x1, 40)
    
    if x1 < BASE - 60:
        ventana_principal.after(100, mover_carro_1)
    else:
        if not hay_ganador:
            hay_ganador = True
            c.create_text(BASE // 2, ALTURA // 2, text="¡¡GANÓ EL CARRO ROJO!!", fill="#FF0055", font=("Arial", 22, "bold"), justify="center")

def mover_carro_2(event=None):
    global x2, carro_2, hay_ganador, img_carro_2

    if 'carro_2' not in globals():
        img_carro_2 = PhotoImage(file="img/carro_azul.png")
        carro_2 = c.create_image(x2, 220, image=img_carro_2, anchor=NW)
        
    x2 += random.randint(1, 10)
    c.coords(carro_2, x2, 220)
    
    if x2 < BASE - 60:
        ventana_principal.after(100, mover_carro_2)
    else:
        if not hay_ganador:
            hay_ganador = True
            c.create_text(BASE // 2, ALTURA // 2, text="¡¡GANÓ EL CARRO AZUL!!", fill="#00E5FF", font=("Arial", 22, "bold"), justify="center")

# -----------------
# ventana principal
# -----------------

ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("800x600")
ventana_principal.config(bg="#0F172A") # Fondo azul muy oscuro

# frame de graficacion
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="#00E5FF", width=780, height=380) # Borde turquesa
frame_graficacion.place(x=10, y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="#1E293B") # Fondo gris azulado
c.place(x=10, y=10)

carretera = c.create_rectangle(0, 10, BASE, 350, fill="#334155", outline="") # Pista asfalto oscuro
L_M = c.create_line(0, 180, BASE, 180, fill="#FACC15", width=6) # Línea central amarilla brillante

# frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="#1E293B", width=780, height=180)
frame_controles.place(x=10, y=410)

texto_controles = Label(frame_controles, text="PRESIONA EL BOTÓN PARA INICIAR LA CARRERA", font=("Arial", 14, "bold"), bg="#1E293B", fg="#F8FAFC", justify="center")
texto_controles.place(x=150, y=20)

carro_uno = Label(frame_controles, text="Carro Rojo", font=("Arial", 12, "bold"), bg="#1E293B", fg="#FF0055")
carro_uno.place(x=150, y=60)

carro_dos = Label(frame_controles, text="Carro Azul", font=("Arial", 12, "bold"), bg="#1E293B", fg="#00E5FF")
carro_dos.place(x=550, y=60)

Img_B = PhotoImage(file="img/carro_rojo.png")
lbl_B = Label(frame_controles, image=Img_B, bg="#1E293B")
lbl_B.image = Img_B
lbl_B.place(x=150, y=90)

Img_c = PhotoImage(file="img/carro_azul.png")
lbl_c = Label(frame_controles, image=Img_c, bg="#1E293B")
lbl_c.image = Img_c
lbl_c.place(x=550, y=90)

b_i = Button(frame_controles, text="Iniciar Carrera", font=("Arial", 13, "bold"), bg="#00E5FF", fg="#0F172A", activebackground="#38BDF8", activeforeground="#0F172A", relief="flat", cursor="hand2", padx=10, pady=5, command=iniciar_carrera)
b_i.place(x=320, y=100)


# desplegar ventana


ventana_principal.mainloop()
