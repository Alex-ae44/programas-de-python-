# Fecha: 2024/11/12
# Elaborado por: alejandro acosta
nombre = "Edinguer"
edad = 19
calificación = 87

# Método 1: Concatenación con conversión explícita
print("Mi nombre es: " + nombre + ", mi edad es: " + str(edad) + ", mi calificación es: " + str(calificación))

# Método 2: Uso de f-strings
print(f"Mi nombre es: {nombre}, mi edad es: {edad}, mi calificación es: {calificación}")

# Método 3: Uso de formato antiguo (%)
print("Mi nombre es: %s, mi edad es: %d, mi calificación es: %.2f" % (nombre, edad, calificación))
