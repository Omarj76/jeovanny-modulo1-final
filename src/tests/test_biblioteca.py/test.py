import sqlite3
import unittest
from datetime import datetime, timedelta

# --- 1. LÓGICA DEL SISTEMA (Clase Biblioteca) ---
class Biblioteca:
    def __init__(self, db_name="talento_libros.db"):
        # Conectamos a la base de datos
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._crear_tablas()

    def _crear_tablas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS libros 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, disponible INTEGER)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS prestamos 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, libro_id INTEGER, usuario TEXT, fecha_entrega TEXT)''')
        self.conn.commit()

    def registrar_libro(self, titulo, autor):
        self.cursor.execute("INSERT INTO libros (titulo, autor, disponible) VALUES (?, ?, 1)", (titulo, autor))
        self.conn.commit()

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

# --- 2. SCRIPT DE PRUEBAS CORREGIDO ---
class TestSistemaBiblioteca(unittest.TestCase):
    def setUp(self):
        # Usamos :memory: para que cada test sea independiente y rápido
        self.lib = Biblioteca(":memory:")
        # Insertamos un libro de prueba. Al ser el primero, su ID será 1
        self.lib.registrar_libro("IA para Todos", "Andrew Ng")

    def test_prestamo_exitoso(self):
        mensaje = self.lib.prestar_libro(1, "Usuario Beta")
        self.assertIn("Préstamo realizado", mensaje)
        
        fecha_esperada = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
        self.assertIn(fecha_esperada, mensaje)

    def test_bloqueo_doble_prestamo(self):
        self.lib.prestar_libro(1, "Usuario A")
        # El segundo intento debe fallar porque el libro ya no está disponible
        segundo_intento = self.lib.prestar_libro(1, "Usuario B")
        self.assertEqual(segundo_intento, "Libro no disponible o no existe.")

# --- 3. EJECUCIÓN ---
if __name__ == "__main__":
    # Esto ejecuta los tests automáticamente
    print("Ejecutando pruebas de calidad de Talento Solutions...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)