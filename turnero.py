class Turnero:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, nombre):
        self.turnos.append(nombre)
        print(f"Turno agregado para: {nombre}")

    def mostrar_turnos(self):
        if not self.turnos:
            print("No hay turnos en la lista.")
        else:
            print("Turnos en la lista:")
            for i, nombre in enumerate(self.turnos, start=1):
                print(f"{i}. {nombre}")

    def atender_turno(self):
        if not self.turnos:
            print("No hay turnos para atender.")
        else:
            atendido = self.turnos.pop(0)
            print(f"Turno atendido: {atendido}")

def main():
    turnero = Turnero()
    
    while True:
        print("\n--- Menú Turnero ---")
        print("1. Agregar turno")
        print("2. Mostrar turnos")
        print("3. Atender turno")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre del cliente: ")
            turnero.agregar_turno(nombre)
        elif opcion == '2':
            turnero.mostrar_turnos()
        elif opcion == '3':
            turnero.atender_turno()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()