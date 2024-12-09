
# Fecha: 2024/01/4
# Elaborado por: alejandro acosta

# Lista de tareas
tareas = ["Comprar comida", "Estudiar Python", "Ir al gimnasio", "Llamar a mamá"]

print("Lista inicial de tareas:", tareas)

# Eliminar y mostrar la última tarea
ultima_tarea = tareas.pop()
print("\nTarea eliminada:", ultima_tarea)

# Eliminar y mostrar una tarea específica por índice
indice = 1
tarea_especifica = tareas.pop(indice)
print("\nTarea eliminada en el índice", indice, ":", tarea_especifica)

# Mostrar la lista de tareas actualizada
print("\nLista de tareas actualizada:", tareas)
