# En este apartado vamos a crear una función que reciba dos números y devuelva el mayor

def mayor(a, b,):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Los números son iguales"
print("El mayor entre 12 y 12 es: ", mayor(12, 12))