# modulo para el manejo de la base de datos
import controlAdministrador
import controlBaseDatos
# coneccion con la base de datos
dbUsuarios = controlBaseDatos.iniciarUsuarios()
dbProductos = controlBaseDatos.iniciarProductos()
dbHistorial = controlBaseDatos.iniciarHistorial()


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
        for i in dbHistorial:
            print(i)
        main()
    # cierra el programa del usuario y regresa al menu principal
    else:
        print("Adios Usuario!")
        import CafeMATEnLinea
        CafeMATEnLinea.main()


# requiere la informacion de pedido del usuario
def realizarPedido():
    controlAdministrador.mostrarMenu()
    cantidadProductos = int(input("Ingrese cuantos productos desea comprar: "))
    pedido = requerirPedido(cantidadProductos)
    confirmarPedido(pedido, cantidadProductos)


# confirma con el usuario que su pedido este correcto
def confirmarPedido(pedido, cantidadProductos):
    precioProducto = []
    nombreProducto = []
    sumaPrecio = float(0)
    sumaProducto = ""
    for i in range(cantidadProductos):
        producto = controlBaseDatos.buscarProductos(int(pedido[i]))
        precioProducto.append(producto[2])
        nombreProducto.append(producto[1])
        sumaPrecio = sumaPrecio + precioProducto[i]
        sumaProducto = sumaProducto + nombreProducto[i]
    print("Precio Productos {} es: {}".format(sumaProducto, sumaPrecio))
    pedidoCompleto = [(len(dbHistorial)+1), sumaProducto, sumaPrecio]
    confirmacion = input('Esta correcta su orden? "1 = SI o 2 = NO"\n')
    if confirmacion == "1":
        dbHistorial.append(pedidoCompleto)
        controlBaseDatos.mandarPedidos(dbHistorial)
        compraNueva = input('Gracias por su orden, ¿Desea ordenar algo mas?: "1 = SI o 2 = NO"\n')
        if compraNueva == "1":
            dbHistorial.append(pedidoCompleto)
            controlBaseDatos.mandarPedidos(dbHistorial)
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
