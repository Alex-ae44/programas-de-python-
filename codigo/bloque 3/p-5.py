
# Fecha: 2024/10/29
# Elaborado por: alejandro acosta reyes

calificacion = input("¿Cuál es su calificación?")
calificacion = float(calificacion)

if calificacion <= 60:
    print("Insuficiente")
elif calificacion >= 70 and calificacion <= 79:
    print("Suficiente")
elif calificacion >= 80 and calificacion <= 89:
    print("Muy bien")
elif calificacion > 90 and calificacion <= 95:
    print("Notable")
else:
   print("Excelente")

print("¡Gracias por usar mi programa!")