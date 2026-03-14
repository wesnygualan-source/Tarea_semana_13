# En este apartado vamos a crear una función que convierta grados Celcius a Fahrenheit
print("------------------Este es un programa que convierte grados Celcius a Fahrenheit------------------")
print("\n") # Imprimir una línea en blanco para separar el programa del texto anterior

celcius = 0
celcius = float(input("Ingrese la temperatura en grados Celcius: "))
def celsius_a_fahrenheit(celcius): 
    return (celcius * 9/5) + 32 # Devolver el resultado de la conversión utilizando la fórmula (C * 9/5) + 32
print(f"{celcius} grados Celcius son equivalente a {celsius_a_fahrenheit(celcius)}")
