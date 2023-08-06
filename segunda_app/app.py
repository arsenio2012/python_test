import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Declara la variable de conexión como global
global conexion
# Define la tabla de usuarios como una variable global
tabla_usuarios = None

# Crear una tabla de ejemplo con datos ficticios
def crear_tabla_usuarios(tabla):
    global conexion  # Accede a la variable global que ya has creado en iniciar_sesion

    cursor = conexion.cursor()
    # Ejecutamos la consulta para obtener los usuarios
    cursor.execute("SELECT username, email, id_rol, create_at FROM users")
    # Recuperamos todos los resultados de la consulta
    resultados = cursor.fetchall()

    # Ahora puedes hacer lo que necesites con los resultados obtenidos, por ejemplo, imprimirlos
    for username, email, id_rol, create_at in resultados:
        # Insertar algunas filas con datos de ejemplo
        tabla.insert("", "end", values=(username, id_rol))

# Función para mostrar la tabla de usuarios
def usuarios_sistema():
    global tabla_usuarios

    etiqueta_titulo.config(text="Usuarios del sistema")
    
     # Si la tabla no ha sido creada previamente, crea la tabla en el contenedor derecho
    # Destruir la tabla si ya existe antes de crear una nueva
    if tabla_usuarios and tabla_usuarios.winfo_exists():
        tabla_usuarios.destroy()

    estilo = ttk.Style()
    estilo.theme_use("clam")

    tabla_usuarios = ttk.Treeview(contenido, columns=("Usuario", "Rol"), show="headings")
    tabla_usuarios.heading("Usuario", text="Usuario")
    tabla_usuarios.heading("Rol", text="Rol")
    tabla_usuarios.column("Usuario", width=100)
    tabla_usuarios.column("Rol", width=100)
    tabla_usuarios.pack(fill="both", expand=True)

    # Agregar datos a la tabla
    crear_tabla_usuarios(tabla_usuarios)

def opcion2_click():
    global tabla_usuarios
    # Destruir la tabla si existe al seleccionar la opción 2
    if tabla_usuarios:
        tabla_usuarios.destroy()

    etiqueta_titulo.config(text="Opción 2")
    contenido.config(text="Aquí va el contenido de la opción 2")

def opcion3_click():
    etiqueta_titulo.config(text="Opción 3")
    contenido.config(text="Aquí va el contenido de la opción 3")

def iniciar_sesion():
    global conexion  # Accede a la variable global para poder modificarla

    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

     #Establemos una conexón a la base de datos o la creamos si no existe
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="python_test"
    )

    cursor = conexion.cursor()
    cursor.execute("SELECT username FROM users WHERE username = %s AND password = %s", (usuario, contrasena))
    resultado = cursor.fetchone()

    if resultado is not None:
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {usuario}!")
        ventana.withdraw()  # Ocultar la ventana de inicio de sesión

        # Abrir la ventana del dashboard
        ventana_dashboard = tk.Toplevel()
        ventana_dashboard.title("Dashboard")
        ventana_dashboard.configure(bg="white")

        # Obtener el ancho y alto de la pantalla
        ancho_pantalla = ventana_dashboard.winfo_screenwidth()
        alto_pantalla = ventana_dashboard.winfo_screenheight()

        # Establecer el tamaño y posición de la ventana
        ventana_dashboard.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0")

        # Panel vertical izquierdo (Menú)
        panel_izquierdo = tk.Frame(ventana_dashboard, bg="light gray")
        panel_izquierdo.pack(side="left", fill="y")

        # Elementos del menú
        etiqueta_menu = tk.Label(panel_izquierdo, text="Menú", bg="light gray", font=("Arial", 16, "bold"))
        etiqueta_menu.pack(pady=10)

        # Opción 1
        opcion1 = tk.Button(panel_izquierdo, text="Ver usuarios del sistema", bg="white", padx=10, pady=5, command=usuarios_sistema)
        opcion1.pack(pady=5)

        # Opción 2
        opcion2 = tk.Button(panel_izquierdo, text="Opción 2", bg="white", padx=10, pady=5, command=opcion2_click)
        opcion2.pack(pady=5)

        # Opción 3
        opcion3 = tk.Button(panel_izquierdo, text="Opción 3", bg="white", padx=10, pady=5, command=opcion3_click)
        opcion3.pack(pady=5)

        # Contenedor a la derecha
        contenedor_derecho = tk.Frame(ventana_dashboard, bg="white")
        contenedor_derecho.pack(side="right", fill="both", expand=True)

        # Agregar elementos al contenedor derecho
        global etiqueta_titulo, contenido
        etiqueta_titulo = tk.Label(contenedor_derecho, text="Contenido", bg="white", font=("Arial", 16, "bold"))
        etiqueta_titulo.pack(pady=10)

        contenido = tk.Label(contenedor_derecho, text="Aquí va el contenido del menú seleccionado", bg="white")
        contenido.pack(pady=5)

        ventana_dashboard.mainloop()
       
        ventana_dashboard.destroy()
        # Cerramos la conexión
        conexion.close()
    else:
       messagebox.showerror("Inicio de sesión fallido", "Credenciales incorrectas") 

# Crear la ventana de inicio de sesión
ventana = tk.Tk()
ventana.title("Dpworkapp")
ventana.configure(bg="black")

# Establecer el tamaño 
ventana.geometry(f"800x400")

# Ruta del archivo de icono (.ico)
#ruta_icono = "recursos/imagenes/dp.ico"

# Establecer el icono de la ventana
#ventana.iconbitmap(ruta_icono)

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
