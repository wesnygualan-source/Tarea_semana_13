# En este apartado vamos a crear una función que verifique si un número es par

def es_par(a):
    if a % 2 == 0: # Verificar si el número a es divisible por 2 sin dejar residuo
        return "El número es par" # Devolver un mensaje indicando que el número es par
    else:
        return "El número es impar" # Devolver un mensaje indicando que el número es impar
print("El número 10 es: ", es_par(10)) # Llamar a la función es_par con el argumento 10 y mostrar el resultado en la consola
print("El número 11 es: ", es_par(11)) # Llamar a la función es_par con el argumento 11 y mostrar el resultado en la consola