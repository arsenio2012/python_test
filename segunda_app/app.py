import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os
import datetime

# Declara la variable de conexión como global
global conexion
# Define la tabla de usuarios como una variable global
tabla_usuarios = None
# Definir el botón de crear usuario en un ámbito global
boton_crear_usuario = None

# Función para cerrar sesión
def cerrar_sesion(ventana_dashboard):
    # Cerrar la ventana del dashboard
    ventana_dashboard.destroy()

    # Mostrar la ventana de inicio de sesión nuevamente
    ventana.destroy()

# Crear una tabla de ejemplo con datos ficticios
def crear_tabla_usuarios(tabla):
    global conexion  # Accede a la variable global que ya has creado en iniciar_sesion

     # Eliminar todos los elementos de la tabla antes de actualizar
    tabla.delete(*tabla.get_children())

    cursor = conexion.cursor()
    # Ejecutamos la consulta para obtener los usuarios
    cursor.execute("SELECT username, email, id_rol, create_at FROM users")
    # Recuperamos todos los resultados de la consulta
    resultados = cursor.fetchall()

    # Ahora puedes hacer lo que necesites con los resultados obtenidos, por ejemplo, imprimirlos
    for username, email, id_rol, create_at in resultados:
        # Insertar algunas filas con datos de ejemplo
        tabla.insert("", "end", values=(username, id_rol))

def crear_usuario():
   # Crear la ventana de registro de usuario
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Dpworkapp - Crear Usuario")
    ventana_registro.configure(bg="#f0f0f0")  # Color de fondo

    # Crear un marco para el formulario con un borde suave
    formulario_frame = tk.Frame(ventana_registro, bg="#ffffff", padx=20, pady=20, borderwidth=2, relief="groove")
    formulario_frame.pack(padx=20, pady=20)

    # Cargar el icono y ajustar su tamaño
    icono = tk.PhotoImage(file="recursos/imagenes/dp.png")  # Reemplaza "ruta_del_icono.png" con la ruta de tu icono
    icono_resized = icono.subsample(2, 2)  # Ajustar el tamaño según tus necesidades
    icono_label = tk.Label(formulario_frame, image=icono_resized, bg="#ffffff")
    icono_label.pack()

    # Etiqueta de título
    etiqueta_titulo = tk.Label(formulario_frame, text="Registrar Nuevo Usuario", font=("Helvetica", 14, "bold"), bg="#ffffff")
    etiqueta_titulo.pack(pady=10)

    # Etiqueta y campo de entrada para el nombre de usuario
    etiqueta_nombre = tk.Label(formulario_frame, text="Nombre de Usuario:", bg="#ffffff")
    etiqueta_nombre.pack()
    entrada_nombre = tk.Entry(formulario_frame)
    entrada_nombre.pack(pady=5)

    # Etiqueta y campo de entrada para el rol
    etiqueta_rol = tk.Label(formulario_frame, text="Rol:", bg="#ffffff")
    etiqueta_rol.pack()
    entrada_rol = tk.Entry(formulario_frame)
    entrada_rol.pack(pady=5)

    # Etiqueta y campo de entrada para el correo electrónico
    etiqueta_correo = tk.Label(formulario_frame, text="Correo Electrónico:", bg="#ffffff")
    etiqueta_correo.pack()
    entrada_correo = tk.Entry(formulario_frame)
    entrada_correo.pack(pady=5)

    # Etiqueta y campo de entrada para la contraseña
    etiqueta_contrasena = tk.Label(formulario_frame, text="Contraseña:", bg="#ffffff")
    etiqueta_contrasena.pack()
    entrada_contrasena = tk.Entry(formulario_frame, show="*")
    entrada_contrasena.pack(pady=5)

    # Función para guardar el nuevo usuario
    def guardar_usuario():
        nuevo_usuario = entrada_nombre.get()
        rol = entrada_rol.get()
        correo = entrada_correo.get()
        contrasena = entrada_contrasena.get()
        fecha_actual = datetime.date.today()

        try:
            # Abrir un cursor para ejecutar las consultas SQL
            cursor = conexion.cursor()

            # Insertar el nuevo usuario en la base de datos
            consulta = "INSERT INTO users (username, password, email, id_rol, create_at) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(consulta, (nuevo_usuario, contrasena, correo, rol, fecha_actual))
            
            # Hacer commit para guardar los cambios en la base de datos
            conexion.commit()

            # Actualizar la tabla de usuarios mostrada en la interfaz
            crear_tabla_usuarios(tabla_usuarios)

            # Cerrar el cursor
            cursor.close()

            # Cerrar la ventana de registro
            ventana_registro.destroy()

            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")

        except Exception as e:
            # Si ocurre un error, hacer rollback y mostrar un mensaje de error
            conexion.rollback()
            messagebox.showerror("Error", f"No se pudo registrar el usuario: {str(e)}")

    # Botón de guardar con estilo
    boton_guardar = tk.Button(formulario_frame, text="Guardar", bg="#4caf50", fg="white", font=("Helvetica", 12), command=guardar_usuario)
    boton_guardar.pack(pady=10, ipadx=10)



# Función para mostrar la tabla de usuarios
def usuarios_sistema():
    global tabla_usuarios, boton_crear_usuario

    etiqueta_titulo.config(text="Usuarios del sistema")
    
     # Si la tabla no ha sido creada previamente, crea la tabla en el contenedor derecho
    # Destruir la tabla si ya existe antes de crear una nueva
    if tabla_usuarios and tabla_usuarios.winfo_exists():
        tabla_usuarios.destroy()

    # Destruir el botón si existe
    if boton_crear_usuario and boton_crear_usuario.winfo_exists():
        boton_crear_usuario.destroy()    

    estilo = ttk.Style()
    estilo.theme_use("clam")

    tabla_usuarios = ttk.Treeview(contenido, columns=("Usuario", "Rol"), show="headings")
    tabla_usuarios.heading("Usuario", text="Usuario")
    tabla_usuarios.heading("Rol", text="Rol")
    tabla_usuarios.column("Usuario", width=100)
    tabla_usuarios.column("Rol", width=100)
    tabla_usuarios.pack(fill="both", expand=True)

    # Agregar botón "Crear Usuario" al footer
    boton_crear_usuario = tk.Button(contenido, text="Crear Usuario", command=crear_usuario)
    boton_crear_usuario.pack(side="left", padx=10, pady=5)    

    # Agregar datos a la tabla
    crear_tabla_usuarios(tabla_usuarios)

 

def opcion2_click():
    global tabla_usuarios, boton_crear_usuario
    # Destruir la tabla si existe al seleccionar la opción 2
    if tabla_usuarios:
        tabla_usuarios.destroy()

    if boton_crear_usuario:
        boton_crear_usuario.destroy()    

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

        ventana_dashboard.protocol("WM_DELETE_WINDOW", lambda: cerrar_sesion(ventana_dashboard))  # Configurar cierre de ventana

        ventana_dashboard.mainloop()
       
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
