# En este apartado vamos a crear una función que reciba un texto y devuelva su longitud

texto = 0
texto = input(str("Ingrese un texto sin espacios entre palabras: "))
def longitud(texto):
    return len(texto)
print(f"La longitud del texto ingresado es: {longitud(texto)}") 
