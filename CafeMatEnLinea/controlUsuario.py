# modulo para el manejo de la base de datos
import sqlite3
# coneccion con la base de datos
connCafe = sqlite3.connect('CafeMAT.db')
cursorCafe = connCafe.cursor()


# menu principal para los usuarios
def main():
    opcion = int(input("""Bienvenido Usuario
    Opciones Disponibles:
    1. Realizar Pedido
    2. Cambiar Informacion de Perfil
    3. Historial de Compras
    4. Cerrar sesion\n"""))
    if opcion == 1:
        realizarPedido()
    elif opcion == 2:
        # funciones para modificar tabla usuarios
        print("place holder")
    elif opcion == 3:
        # funciones consultar tabla historial
        print("place holder")
    # cierra el programa del usuario y regresa al menu principal
    else:
        print("Adios Usuario!")
        import CafeMATEnLinea
        CafeMATEnLinea.main()


# requiere la informacion de pedido del usuario
def realizarPedido():
    mostrarMenu()
    cantidadProductos = int(input("Ingrese cuantos productos desea comprar: "))
    pedido = requerirPedido(cantidadProductos)
    confirmarPedido(pedido, cantidadProductos)


# confirma con el usuario que su pedido este correcto
def confirmarPedido(pedido, cantidadProductos):
    for i in range(cantidadProductos):
        cursorCafe.execute("SELECT precio FROM productos WHERE ID = ?", (pedido[i],))
        precioProducto = cursorCafe.fetchone()
        cursorCafe.execute("SELECT producto FROM productos WHERE ID = ?", (pedido[i],))
        nombreProducto = cursorCafe.fetchone()
        print("Precio Producto {} es: {}".format(nombreProducto, precioProducto))
    confirmacion = input('Esta correcta su orden? "1 = SI o 2 = NO"\n')
    if confirmacion == "1":
        compraNueva = input('Gracias por su orden, ¿Desea ordenar algo mas?: "1 = SI o 2 = NO"\n')
        if compraNueva == "1":
            # Implementacion de notificacion por correo aqui enviar variable "pedido".
            realizarPedido()
        else:
            main()
    else:
        realizarPedido()


# organiza el pedido del usuario en un arreglo
def requerirPedido(cantidadProductos):
    pedido = []
    print("Ingrese el ID de los productos que desea: ")
    for i in range(int(cantidadProductos)):
        pedido.append(input('producto {}:'.format(i + 1)))
    return pedido


# imprime el menu de productos
def mostrarMenu():
    cursorCafe.execute("SELECT * FROM productos")
    print('(ID, PRODUCTO, PRECIO)')
    for producto in cursorCafe.fetchall():
        print(producto)
