# En este apartado vamos a crear una función para obtener el total de precio de un producto
print("-------BIENVENIDOS A LA CALCULADORA PARA DETERMINAR EL PRECIO TOTALDE LOS PRODUCTOS--------")
print()
precio = 0 # Definimos una variable llamado precio
cantidad = 0 # Definimos una variable llamada cantidad
precio = float(input("Ingrese el precio del producto")) # Definimos una entrada de valor decimal
cantidad = int(input("Ingrese la cantidad de producto escogido")) # Definimos una entrada de valor entero
def total_precio(precio, cantidad): # Creamos una variable llamada total_precio con dos parámetros
    return precio * cantidad # Retornamos los dos paáramtros como producto
print(f"El precio total a pagar del producto es: {total_precio(precio, cantidad)}")