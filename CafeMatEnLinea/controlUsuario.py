import sqlite3

connProductos = sqlite3.connect('productosbd.db')
cursorProductos = connProductos.cursor()


def main():
    cursorProductos.execute("SELECT * FROM productos")
    print('(ID, PRODUCTO, PRECIO)')
    for producto in cursorProductos.fetchall():
        print(producto)
    cantidadProductos = int(input("Ingrese cuantos productos desea comprar: "))
    pedido = requerirPedido(cantidadProductos)
    confirmarPedido(pedido, cantidadProductos)



def confirmarPedido(pedido, cantidadProductos):
    for i in range(cantidadProductos):
        cursorProductos.execute("SELECT precio FROM productos WHERE ID = ?", (pedido[i],))
        precioProducto = cursorProductos.fetchone()
        cursorProductos.execute("SELECT producto FROM productos WHERE ID = ?", (pedido[i],))
        nombreProducto = cursorProductos.fetchone()
        print("Precio Producto {} es: {}".format(nombreProducto, precioProducto))
    confirmacion = input('Esta correcta su orden? "1 = SI o 2 = NO"\n')
    if confirmacion == "1":
        compraNueva = input('Gracias por su orden, ¿Desea ordenar algo mas?: "1 = SI o 2 = NO"\n')
        if compraNueva == "1":
            # Implementacion de notificacion por correo aqui enviar variable "pedido".
            main()
        else:
            # Implementacion de notificaion por correo aqui enviar variable "pedido".
            cursorProductos.close()
            connProductos.close()
    else:
        main()


def requerirPedido(cantidadProductos):
    pedido = []
    print("Ingrese el ID de los productos que desea: ")
    for i in range(int(cantidadProductos)):
        pedido.append(input('producto {}:'.format(i + 1)))
    return pedido
