class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.tareas.append(tarea)

    def eliminar_tarea(self, indice):
        if indice >= 0 and indice < len(self.tareas):
            del self.tareas[indice]

    def marcar_tarea_completada(self, indice):
        if indice >= 0 and indice < len(self.tareas):
            self.tareas[indice].marcar_completada()

    def mostrar_tareas(self):
        if len(self.tareas) == 0:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i+1}. {tarea}")

# Crear una instancia de la lista de tareas
lista_tareas = ListaTareas()

while True:
    print("Lista de Tareas")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Mostrar tareas")
    print("5. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        descripcion = input("Ingrese la descripción de la tarea: ")
        lista_tareas.agregar_tarea(descripcion)
        print("Tarea agregada exitosamente.")

    elif opcion == 2:
        indice = int(input("Ingrese el índice de la tarea a eliminar: ")) - 1
        lista_tareas.eliminar_tarea(indice)
        print("Tarea eliminada exitosamente.")

    elif opcion == 3:
        indice = int(input("Ingrese el índice de la tarea a marcar como completada: ")) - 1
        lista_tareas.marcar_tarea_completada(indice)
        print("Tarea marcada como completada.")

    elif opcion == 4:
        lista_tareas.mostrar_tareas()

    elif opcion == 5:
        print("Gracias por usar la lista de tareas.")
        break

    else:
        print("Opción incorrecta. Por favor, seleccione una opción válida.")

    print()