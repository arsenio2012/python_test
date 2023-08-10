import mysql.connector

class Database:
    def __init__(self):
        # Inicializar la conexión a la base de datos
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_test"
        )

        self.cursor = self.conn.cursor()

    def ejecutar_query(self, query, parametros=None):
        if parametros:
            self.cursor.execute(query, parametros)
        else:
            self.cursor.execute(query)
        self.conexion.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()