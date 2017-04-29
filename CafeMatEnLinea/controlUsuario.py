import sqlite3
connCafe = sqlite3.connect('CafeMAT.db')
cursorCafe = connCafe.cursor()


def main():
    opcion = int(input("""Bienvenido Usuario
    Opciones Disponibles:
    1. Realizar Pedido
    2. Cambiar Informacion de Perfil
    3. Historial de Compras
    4. Cerrar Programa\n"""))
    if opcion == 1:
        realizarPedido()
    elif opcion == 2:
        # funciones para modificar tabla usuarios
        print("place holder")
    elif opcion == 3:
        # funciones consultar tabla historial
        print("place holder")
    else:
        print("Adios Usuario!")
        import CafeMATEnLinea
        CafeMATEnLinea.main()


def realizarPedido():
    mostrarMenu()
    cantidadProductos = int(input("Ingrese cuantos productos desea comprar: "))
    pedido = requerirPedido(cantidadProductos)
    confirmarPedido(pedido, cantidadProductos)


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


def requerirPedido(cantidadProductos):
    pedido = []
    print("Ingrese el ID de los productos que desea: ")
    for i in range(int(cantidadProductos)):
        pedido.append(input('producto {}:'.format(i + 1)))
    return pedido


def mostrarMenu():
    cursorCafe.execute("SELECT * FROM productos")
    print('(ID, PRODUCTO, PRECIO)')
    for producto in cursorCafe.fetchall():
        print(producto)
