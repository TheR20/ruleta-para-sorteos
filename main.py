import tkinter as tk
import random
import time
import pyttsx3

# Crear el objeto para la conversión de texto a voz
engine = pyttsx3.init()

def sacar_participante():
    global participantes
    if len(participantes) > 1:
        animar_ruleta()
        ventana.after(2000, seleccionar_ganador)
    else:
        etiqueta.config(text="Ya se sacó al último participante.")

def seleccionar_ganador():
    global participantes
    ganador = random.choice(participantes)
    participantes.remove(ganador)
    etiqueta.config(text=f"Perdedor: {ganador}")
    engine.say(f"El perdedor de esta ronda es {ganador}")  # Convertir el nombre del ganador a voz
    engine.runAndWait()
    actualizar_lista_participantes()

def animar_ruleta():
    etiqueta.config(text="La ruleta está girando...")
    for _ in range(5):
        for i in range(len(participantes)):
            etiqueta_participantes.config(text=participantes[i])
            ventana.update()
            time.sleep(0.1)

def reiniciar_rifa():
    global participantes
    participantes = original_participantes[:]
    etiqueta.config(text="Rifa reiniciada. Presiona 'Sacar' para empezar.")
    actualizar_lista_participantes()

def actualizar_lista_participantes():
    etiqueta_participantes.config(text="\n".join(participantes))

# Lista de participantes (puedes agregar más)
original_participantes =  ["Mochila", "Stan", "Cerdo", "Robobot", "TheR20", "ChinoMariconk","Jeremias", "Alex","Mochila", "Stan", "Cerdo", "Robobot", "TheR20", "ChinoMariconk", "Alex","Maitro"]
participantes = original_participantes[:]

# Crear ventana
ventana = tk.Tk()
ventana.title("Rifa con ruleta")
ventana.geometry("400x400")  # Cambiar el tamaño de la ventana

# Etiqueta para mostrar al ganador o mensajes
etiqueta = tk.Label(ventana, text="Presiona 'Sacar' para empezar la rifa.", font=("Arial", 48))  # Aumentar el tamaño de la fuente
etiqueta.pack(pady=20)

# Etiqueta para mostrar la lista de participantes restantes
etiqueta_participantes = tk.Label(ventana, text="\n".join(participantes), font=("Arial", 48))  # Aumentar el tamaño de la fuente
etiqueta_participantes.pack(pady=10)

# Botón para sacar un participante
boton_sacar = tk.Button(ventana, text="Sacar", command=sacar_participante, padx=20, pady=10, bg="red", fg="white")
boton_sacar.pack(pady=10)

# Botón para reiniciar la rifa
boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar_rifa, padx=20, pady=10)
boton_reiniciar.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()

