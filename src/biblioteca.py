import sqlite3
from datetime import datetime, timedelta

class Biblioteca:
    def __init__(self, db_name="talento_libros.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._crear_tablas()

    def _crear_tablas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS libros 
            (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, disponible INTEGER)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS prestamos 
            (id INTEGER PRIMARY KEY, libro_id INTEGER, usuario TEXT, fecha_entrega TEXT)''')
        self.conn.commit()

    def registrar_libro(self, titulo, autor):
        self.cursor.execute("INSERT INTO libros (titulo, autor, disponible) VALUES (?, ?, 1)", (titulo, autor))
        self.conn.commit()
        print(f"Libro '{titulo}' registrado con éxito.")

    def prestar_libro(self, libro_id, usuario):
        self.cursor.execute("SELECT disponible FROM libros WHERE id = ?", (libro_id,))
        res = self.cursor.fetchone()
        if res and res[0] == 1:
            fecha_limite = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
            self.cursor.execute("INSERT INTO prestamos (libro_id, usuario, fecha_entrega) VALUES (?, ?, ?)", 
                                (libro_id, usuario, fecha_limite))
            self.cursor.execute("UPDATE libros SET disponible = 0 WHERE id = ?", (libro_id,))
            self.conn.commit()
            return f"Préstamo realizado a {usuario}. Devolver antes de: {fecha_limite}"
        return "Libro no disponible o no existe."

    def devolver_libro(self, prestamo_id):
        self.cursor.execute("SELECT libro_id FROM prestamos WHERE id = ?", (prestamo_id,))
        res = self.cursor.fetchone()
        if res:
            self.cursor.execute("UPDATE libros SET disponible = 1 WHERE id = ?", (res[0],))
            self.cursor.execute("DELETE FROM prestamos WHERE id = ?", (prestamo_id,))
            self.conn.commit()
            return "Libro devuelto con éxito."
        return "Préstamo no encontrado."

    def listar_libros(self):
        self.cursor.execute("SELECT id, titulo, autor, disponible FROM libros")
        return self.cursor.fetchall()

    def cerrar(self):
        self.conn.close()