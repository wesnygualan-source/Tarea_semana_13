// En este apartado vamos a crear una función que permita encontrar el valor total entre precio y cantidad


public class Tarea_semana_13 {

    // Función que calcula el total
    static int total_compra(int precio, int cantidad) {
        return precio * cantidad;
    }

    public static void main(String[] args) {
        System.out.println("--------------Este es un programa para encontrar el valor total del precio de un producto-------------");
        System.out.println(); // Este es un salto de línea
        System.out.println("El total del producto es: " + total_compra(10, 3));
    }
}
