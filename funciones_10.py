# En este apartado vamos a crear una función que devuelva el valor absoluto de un número
print("------------------Este es un programa que devuelve el valor absoluto de un número------------------")
print("\n") # Imprimir una línea en blanco para separar el programa del texto anterior

numero = 0
numero = float(input("Ingrese un número: "))
def absoluto(numero):
    if numero < 0:
        return -numero
    else:
        return numero
print(f"El valor absoluto de {numero} es: {absoluto(numero)}")