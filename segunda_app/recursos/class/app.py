import tkinter as tk
from tkinter import messagebox
from database import Database

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Dpworkapp")
        self.root.configure(bg="black")

        self.db = Database()  # Crear una instancia de la clase Database

        # Crear elementos de la interfaz gráfica
        # ...

        # Conectar eventos a métodos
        # ...