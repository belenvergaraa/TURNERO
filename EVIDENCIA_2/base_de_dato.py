import sqlite3

class Turnero:
    def __init__(self):
        # Conexión a la base de datos
        self.conn = sqlite3.connect('turnero.db')
        self.cursor = self.conn.cursor()
        # Crear tabla si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS turnos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                fecha_creacion DATE DEFAULT (DATE('now')),
                estado TEXT CHECK(estado IN ('pendiente', 'atendido')) DEFAULT 'pendiente'
            )
        ''')
        self.conn.commit()

    def agregar_turno(self, nombre):
        self.cursor.execute('INSERT INTO turnos (nombre) VALUES (?)', (nombre,))
        self.conn.commit()
        print(f"Turno agregado para: {nombre}")

    def mostrar_turnos(self):
        self.cursor.execute('SELECT * FROM turnos')
        turnos = self.cursor.fetchall()
        if not turnos:
            print("No hay turnos en la lista.")
        else:
            print("Turnos en la lista:")
            for (id, nombre, fecha, estado) in turnos:
                print(f"ID: {id}, Nombre: {nombre}, Fecha: {fecha}, Estado: {estado}")

    def atender_turno(self):
        self.cursor.execute('SELECT * FROM turnos WHERE estado = "pendiente" LIMIT 1')
        turno = self.cursor.fetchone()
        if not turno:
            print("No hay turnos pendientes para atender.")
        else:
            self.cursor.execute('UPDATE turnos SET estado = "atendido" WHERE id = ?', (turno[0],))
            self.conn.commit()
            print(f"Turno atendido: {turno[1]}")

    def consultas(self):
        print("\nConsulta de estados:")
        self.cursor.execute('SELECT estado, COUNT(*) as cantidad FROM turnos GROUP BY estado')
        for row in self.cursor.fetchall():
            print(f"Estado: {row[0]}, Cantidad: {row[1]}")

        print("\nTurnos con nombre que contiene 'Juan':")
        self.cursor.execute('SELECT * FROM turnos WHERE nombre LIKE ?', ('%Juan%',))
        for row in self.cursor.fetchall():
            print(row)

        print("\nTurnos atendidos:")
        self.cursor.execute('SELECT * FROM turnos WHERE estado = "atendido"')
        for row in self.cursor.fetchall():
            print(row)

    def cerrar(self):
        self.conn.close()

def main():
    turnero = Turnero()
    
    # Opciones del menú
    while True:
        print("\n--- Menú Turnero ---")
        print("1. Agregar turno")
        print("2. Mostrar turnos")
        print("3. Atender turno")
        print("4. Consultas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            turnero.agregar_turno(nombre)
        elif opcion == '2':
            turnero.mostrar_turnos()
        elif opcion == '3':
            turnero.atender_turno()
        elif opcion == '4':
            turnero.consultas()
        elif opcion == '5':
            turnero.cerrar()
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()