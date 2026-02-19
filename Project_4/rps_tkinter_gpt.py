import tkinter as tk
import random

# -------------------------------
# Función principal del juego
# -------------------------------
def jugar(eleccion_usuario):
    opciones = ['Piedra', 'Papel', 'Tijeras']
    eleccion_computadora = random.choice(opciones)

    if eleccion_usuario == eleccion_computadora:
        resultado = "Empate 🤝"
    elif (eleccion_usuario == 'Piedra' and eleccion_computadora == 'Tijeras') or \
         (eleccion_usuario == 'Papel' and eleccion_computadora == 'Piedra') or \
         (eleccion_usuario == 'Tijeras' and eleccion_computadora == 'Papel'):
        resultado = "¡Ganaste! 🎉"
    else:
        resultado = "Perdiste 😢"

    etiqueta_resultado.config(
        text=f"Tú: {eleccion_usuario}\nComputadora: {eleccion_computadora}\n\n{resultado}"
    )

# -------------------------------
# Función para reiniciar el juego
# -------------------------------
def reiniciar():
    etiqueta_resultado.config(text="Haz tu elección para comenzar.")

# -------------------------------
# Configuración de la ventana
# -------------------------------
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijeras")
ventana.geometry("300x400")
ventana.config(bg="#f0f0f0")

# -------------------------------
# Etiquetas y botones
# -------------------------------
titulo = tk.Label(ventana, text="🪨📄✂️ Piedra, Papel o Tijeras", font=("Arial", 14, "bold"), bg="#f0f0f0")
titulo.pack(pady=15)

etiqueta_resultado = tk.Label(ventana, text="Haz tu elección para comenzar.", font=("Arial", 12), bg="#f0f0f0", justify="center")
etiqueta_resultado.pack(pady=20)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=10)

botones = [
    ("Piedra 🪨", "Piedra"),
    ("Papel 📄", "Papel"),
    ("Tijeras ✂️", "Tijeras")
]

for texto, valor in botones:
    tk.Button(
        frame_botones,
        text=texto,
        font=("Arial", 12),
        width=10,
        command=lambda v=valor: jugar(v)
    ).pack(pady=5)

# Botón de reinicio
tk.Button(
    ventana,
    text="Reiniciar 🔁",
    font=("Arial", 11),
    bg="#d0d0d0",
    command=reiniciar
).pack(pady=15)

# -------------------------------
# Ejecutar ventana
# -------------------------------
ventana.mainloop()
