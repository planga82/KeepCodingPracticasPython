# Ejercicio 4
import math

try:
    numeros=[]
    for numero in range(3):
        entrada = raw_input("Introduzca numero: ")
        numeros.append(float(entrada))

    #Calculo de la media
    media = sum(numeros)*1.0/len(numeros)
    #Dicido el numero en la parte entera y decimal
    splitNumero = str(media).split(".")
    parteEntera = splitNumero[0]
    parteDecimal = splitNumero[1]
    truncadoParteDecimal = list(parteDecimal)[0]
    print('La media es: ' + parteEntera + "." + truncadoParteDecimal)
except ValueError:
    print('No ha introdcido un numero: ' + entrada)