import tkinter as tk
from tkinter import messagebox

def iniciar_sesion():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    # Verificar las credenciales de inicio de sesión
    if usuario == "admin" and contrasena == "123456":
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {usuario}!")
        ventana.withdraw()  # Ocultar la ventana de inicio de sesión

        # Abrir la ventana del dashboard
        ventana_dashboard = tk.Toplevel()
        ventana_dashboard.title("Dashboard")
        ventana_dashboard.configure(bg="white")

        # Panel vertical izquierdo (Menú)
        panel_izquierdo = tk.Frame(ventana_dashboard, bg="light gray")
        panel_izquierdo.pack(side="left", fill="y")

        # Elementos del menú
        etiqueta_menu = tk.Label(panel_izquierdo, text="Menú", bg="light gray", font=("Arial", 16, "bold"))
        etiqueta_menu.pack(pady=10)

        # Opción 1
        opcion1 = tk.Button(panel_izquierdo, text="Opción 1", bg="white", padx=10, pady=5)
        opcion1.pack(pady=5)

        # Opción 2
        opcion2 = tk.Button(panel_izquierdo, text="Opción 2", bg="white", padx=10, pady=5)
        opcion2.pack(pady=5)

        # Opción 3
        opcion3 = tk.Button(panel_izquierdo, text="Opción 3", bg="white", padx=10, pady=5)
        opcion3.pack(pady=5)

        # Contenedor a la derecha
        contenedor_derecho = tk.Frame(ventana_dashboard, bg="white")
        contenedor_derecho.pack(side="right", fill="both", expand=True)

        # Agregar elementos al contenedor derecho
        etiqueta_titulo = tk.Label(contenedor_derecho, text="Contenido", bg="white", font=("Arial", 16, "bold"))
        etiqueta_titulo.pack(pady=10)

        contenido = tk.Label(contenedor_derecho, text="Aquí va el contenido del menú seleccionado", bg="white")
        contenido.pack(pady=5)

        ventana_dashboard.mainloop()
    else:
        messagebox.showerror("Inicio de sesión fallido", "Credenciales incorrectas")

# Crear la ventana de inicio de sesión
ventana = tk.Tk()
ventana.title("Dpworkapp")
ventana.configure(bg="black")

# Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Establecer el tamaño y posición de la ventana
ventana.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

# Agregar un marco que ocupe todo el espacio
marco = tk.Frame(ventana, bg="black")
marco.place(relwidth=1, relheight=1)

# Crear un marco para el formulario
formulario_frame = tk.Frame(marco, bg="black", bd=5)
formulario_frame.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.3, anchor="center")

# Etiqueta de usuario
usuario_label = tk.Label(formulario_frame, text="Usuario:", bg="black", fg="white")
usuario_label.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.2)

# Cuadro de entrada de usuario
usuario_entry = tk.Entry(formulario_frame, bg="white")
usuario_entry.place(relx=0.4, rely=0.2, relwidth=0.5, relheight=0.2)

# Etiqueta de contraseña
contrasena_label = tk.Label(formulario_frame, text="Contraseña:", bg="black", fg="white")
contrasena_label.place(relx=0.1, rely=0.5, relwidth=0.3, relheight=0.2)

# Cuadro de entrada de contraseña
contrasena_entry = tk.Entry(formulario_frame, show="*", bg="white")
contrasena_entry.place(relx=0.4, rely=0.5, relwidth=0.5, relheight=0.2)

# Botón de inicio de sesión
boton_iniciar_sesion = tk.Button(formulario_frame, text="Iniciar sesión", command=iniciar_sesion)
boton_iniciar_sesion.place(relx=0.4, rely=0.8, relwidth=0.5, relheight=0.2)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
