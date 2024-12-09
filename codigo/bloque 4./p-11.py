
# Fecha: 2024/11/8
# Elaborado por:alejandro acosta

# Inicializaciòn de variable
palabra = ""
while palabra != "salir":
    palabra = input("Ingresa una palabra o 'salir' para terminar: ")
    palabra = palabra.lower() #  Convierte la palabra a minusculas
    print("Usted ingreso: ", palabra)
print("Fin del programa")
