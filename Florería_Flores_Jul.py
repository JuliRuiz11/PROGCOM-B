import tkinter as tk
from tkinter import messagebox
import random
import os

# ---------- CREACIÓN DEL INVENTARIO ----------
def crear_inventario():
    flores = [
        "orquídea negra",
        "flor de loto azul",
        "ave del paraíso",
        "protea real",
        "cala negra",
        "hibisco tropical",
        "dalia de fuego",
        "orquídea fantasma",
        "jazmín de Madagascar",
        "rosa arcoíris",
        "tulipán negro",
        "flor de jade",
        "lirio estelar",
        "magnolia púrpura"
    ]
    return {
        flor: {
            "precio": random.randint(25000, 80000),
            "cantidad": random.randint(5, 25),
            "vendidas": 0,
            "reservadas": 0
        } for flor in flores
    }

inventario = crear_inventario()
total_ganado = 0
reservas_realizadas = 0
flores_vendidas = 0
limite_reservas = 20
archivo_reservas = "reservas.txt"

# Reiniciar archivo de reservas
with open(archivo_reservas, "w", encoding="utf-8") as f:
    f.write("🌸 Reservas del día - Floristería Flores Jul 🌸\n\n")

# ---------- FUNCIONES ----------
def vender():
    global total_ganado, flores_vendidas
    flor = flor_var.get()
    try:
        cantidad = int(cantidad_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida")
        return
    if flor not in inventario:
        messagebox.showerror("Error", f"{flor} no está disponible")
        return
    datos = inventario[flor]
    if cantidad > datos["cantidad"]:
        messagebox.showwarning("Stock insuficiente", "No hay suficiente cantidad disponible")
        return
    datos["cantidad"] -= cantidad
    datos["vendidas"] += cantidad
    flores_vendidas += cantidad
    venta = datos["precio"] * cantidad
    total_ganado += venta
    messagebox.showinfo("Venta realizada", f"Vendidas {cantidad} de {flor} por ${venta:,}")
    if datos["cantidad"] == 0:
        del inventario[flor]
        actualizar_menu()

def reservar():
    global reservas_realizadas
    flor = flor_var.get()
    nombre = nombre_entry.get().strip()
    try:
        cantidad = int(cantidad_reserva_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Cantidad inválida")
        return
    if not nombre:
        messagebox.showwarning("Falta nombre", "Por favor escribe el nombre del cliente.")
        return
    if flor not in inventario:
        messagebox.showerror("Error", f"{flor} no está disponible")
        return
    if reservas_realizadas + cantidad > limite_reservas:
        disponibles = max(0, limite_reservas - reservas_realizadas)
        messagebox.showwarning("Límite alcanzado",
                               f"Solo puedes hacer {disponibles} reservas más hoy (máximo {limite_reservas} por día).")
        return
    inventario[flor]["reservadas"] += cantidad
    reservas_realizadas += cantidad
    restantes = limite_reservas - reservas_realizadas
    with open(archivo_reservas, "a", encoding="utf-8") as f:
        f.write(f"Cliente: {nombre} | Flor: {flor} | Cantidad: {cantidad}\n")
    messagebox.showinfo("Reserva confirmada",
                        f"Reserva registrada para {nombre} 🌸\n{cantidad} de {flor}\nReservas restantes hoy: {restantes}")
    nombre_entry.delete(0, tk.END)
    cantidad_reserva_entry.delete(0, tk.END)

def ver_reservas():
    if not os.path.exists(archivo_reservas):
        messagebox.showinfo("Reservas", "No hay reservas registradas.")
        return
    with open(archivo_reservas, "r", encoding="utf-8") as f:
        contenido = f.read()
    messagebox.showinfo("Reservas del día", contenido)

def añadir_flor():
    nombre = nueva_flor_entry.get().strip().lower()
    try:
        precio = int(precio_entry.get())
        cantidad = int(cantidad_nueva_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Precio o cantidad inválidos")
        return
    if nombre in inventario:
        messagebox.showwarning("Ya existe", "La flor ya está en el inventario")
        return
    inventario[nombre] = {
        "precio": precio,
        "cantidad": cantidad,
        "vendidas": 0,
        "reservadas": 0
    }
    actualizar_menu()
    messagebox.showinfo("Flor añadida", f"{nombre.title()} añadida con éxito 🌺")

def eliminar_flor():
    flor = flor_var.get()
    if flor in inventario:
        del inventario[flor]
        actualizar_menu()
        messagebox.showinfo("Flor eliminada", f"{flor.title()} fue eliminada del inventario")

def mostrar_total_flores():
    if not inventario:
        messagebox.showinfo("Inventario", "No hay flores en el almacén.")
        return
    total = sum(datos["cantidad"] for datos in inventario.values())
    detalle = "\n".join([
        f"{flor.title()}: {datos['cantidad']} unidades - ${datos['precio']:,} c/u - Reservadas: {datos['reservadas']}"
        for flor, datos in inventario.items()
    ])
    mensaje = f"Total de flores en almacén: {total} unidades\n\nDetalle:\n{detalle}"
    messagebox.showinfo("Inventario total", mensaje)

def actualizar_menu():
    flor_menu['menu'].delete(0, 'end')
    for flor in inventario:
        flor_menu['menu'].add_command(label=flor, command=tk._setit(flor_var, flor))
    flor_var.set(next(iter(inventario), ""))

def cerrar_tienda():
    total_reservadas = sum(d['reservadas'] for d in inventario.values())
    total_restantes = sum(d['cantidad'] for d in inventario.values())
    resumen = (
        f"💐 Floristería Flores Jul 💐\n\n"
        f"🌸 Total flores vendidas: {flores_vendidas}\n"
        f"🌺 Total flores reservadas: {reservas_realizadas}\n"
        f"🌿 Flores restantes en inventario: {total_restantes}\n\n"
        f"💰 Total ganado: ${total_ganado:,}"
    )
    messagebox.showinfo("Resumen del día", resumen)

# ---------- INTERFAZ ----------
ventana = tk.Tk()
ventana.title("💐 Florería Flores Jul 💐")
ventana.geometry("480x750")
ventana.config(bg="#E3F2FD")

tk.Label(ventana, text="Bienvenida a la Florería Flores Jul 🌷", font=("Century Gothic", 15, "bold"), bg="#E3F2FD", fg="#4A148C").pack(pady=15)
flor_var = tk.StringVar()
flor_var.set(next(iter(inventario)))
tk.Label(ventana, text="Selecciona una flor exótica:", bg="#E3F2FD", font=("Arial", 11)).pack()
flor_menu = tk.OptionMenu(ventana, flor_var, *inventario.keys())
flor_menu.config(bg="#C5CAE9", font=("Arial", 10))
flor_menu.pack(pady=5)

tk.Label(ventana, text="Cantidad a vender:", bg="#E3F2FD", font=("Arial", 11)).pack()
cantidad_entry = tk.Entry(ventana)
cantidad_entry.pack(pady=3)
tk.Button(ventana, text="Vender", command=vender, bg="#7E57C2", fg="white", font=("Arial", 10, "bold")).pack(pady=6)

tk.Label(ventana, text="Reservar flor exótica 🌺", bg="#E3F2FD", font=("Century Gothic", 12, "bold")).pack(pady=10)
tk.Label(ventana, text="Nombre del cliente:", bg="#E3F2FD").pack()
nombre_entry = tk.Entry(ventana)
nombre_entry.pack(pady=3)
tk.Label(ventana, text="Cantidad a reservar:", bg="#E3F2FD").pack()
cantidad_reserva_entry = tk.Entry(ventana)
cantidad_reserva_entry.pack(pady=3)
tk.Button(ventana, text="Hacer reserva", command=reservar, bg="#64B5F6", fg="white", font=("Arial", 10, "bold")).pack(pady=6)
tk.Button(ventana, text="Ver reservas del día", command=ver_reservas, bg="#4FC3F7", fg="white", font=("Arial", 10, "bold")).pack(pady=6)

tk.Button(ventana, text="Eliminar flor seleccionada", command=eliminar_flor, bg="#BA68C8", fg="white", font=("Arial", 10, "bold")).pack(pady=6)
tk.Button(ventana, text="Ver total de flores", command=mostrar_total_flores, bg="#7986CB", fg="white", font=("Arial", 10, "bold")).pack(pady=6)

tk.Label(ventana, text="Añadir nueva flor exótica 🌸", bg="#E3F2FD", font=("Century Gothic", 12, "bold")).pack(pady=10)
tk.Label(ventana, text="Nombre:", bg="#E3F2FD").pack()
nueva_flor_entry = tk.Entry(ventana)
nueva_flor_entry.pack(pady=3)
tk.Label(ventana, text="Precio:", bg="#E3F2FD").pack()
precio_entry = tk.Entry(ventana)
precio_entry.pack(pady=3)
tk.Label(ventana, text="Cantidad:", bg="#E3F2FD").pack()
cantidad_nueva_entry = tk.Entry(ventana)
cantidad_nueva_entry.pack(pady=3)
tk.Button(ventana, text="Añadir flor", command=añadir_flor, bg="#81D4FA", fg="white", font=("Arial", 10, "bold")).pack(pady=8)
tk.Button(ventana, text="Cerrar tienda", command=cerrar_tienda, bg="#512DA8", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

ventana.mainloop()
