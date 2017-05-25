import controlBaseDatos

dbUsuarios = controlBaseDatos.iniciarUsuarios()
dbProductos = controlBaseDatos.iniciarProductos()
dbHistorial = controlBaseDatos.iniciarHistorial()

# menu principal del administrador
def main():
    opcion = int(input("""Bienvenido Administrador
Seleccione la opcion deseada:
1. Eliminar Usuario
2. Modificar Menu
3. Notificar Usuario
4. Consultar Ordenes
5. Bannear Usuario
6. Actualizar Base de Datos
7. Cerrar Sesión\n"""))
    if opcion == 1:
        eliminarUsuarios()
    elif opcion == 2:
        modificarMenu()
    elif opcion == 3:
        notificarUsuario()
    elif opcion == 4:
        controlBaseDatos.consultarOrdenes(dbHistorial)
    elif opcion == 5:
        bangarang()
    elif opcion == 6:
        controlBaseDatos.mandarUsuarios(dbUsuarios)
        controlBaseDatos.mandarProductos(dbProductos)
        controlBaseDatos.mandarPedidos(dbHistorial)
    else:
        print("Adios Administrador!")
        import CafeMATEnLinea
        controlBaseDatos.mandarUsuarios(dbUsuarios)
        controlBaseDatos.mandarProductos(dbProductos)
        controlBaseDatos.mandarPedidos(dbHistorial)
        CafeMATEnLinea.main()


# funcion para la eliminacion de usuarios
def eliminarUsuarios():
    controlBaseDatos.mostrarUsuarios(dbUsuarios)
    reset = 1
    eliminado = int(input("Escriba el ID del usuario que desea eliminar\n"))-1
    # confirma si se desea eliminar al usuario seleccionado
    confirmacion = input("Desea eliminar a {}? '1 = SI' o '2 = NO'\n".format(dbUsuarios[eliminado]))
    if confirmacion == '1':
        del dbUsuarios[eliminado]
        for reset in range((len(dbUsuarios))):
            dbUsuarios[reset][0] = reset+1
        # confirma si se desea regresar al menu principal
        regresar = input("Desea regresar al menu principal? '1 = SI' o '2 = NO'\n")
        if regresar == '1':
            main()
        else:
            eliminarUsuarios()
    else:
        regresar = input("Desea regresar al menu principal? '1 = SI' o '2 = NO'\n")
        if regresar == '1':
            main()
        else:
            eliminarUsuarios()


# menu para la modificacion de los productos en el menu
def modificarMenu():
    opcion = int(input("""Opciones Disponibles
    1. Modificar Producto Existente
    2. Agregar Nuevo Producto
    3. Eliminar Producto Existente
    4. Regresar al Menu Principal\n"""))
    if opcion == 1:
            modificarProducto()
    elif opcion == 2:
            agregarProducto()
    elif opcion == 3:
            eliminarProducto()
    else:
        main()


# menu para elegir que se requiere modificar de algun producto en el menu
def modificarProducto():
    opcion = int(input("""¿Que Desea Modificar?
    Opciones Disponibles
    1. Modificar Nombre
    2. Modificar Precio
    3. Elegir otro producto
    4. Regresar al Menu Principal\n"""))
    if opcion == 1:
            modificarNombre()
    elif opcion == 2:
            modificarPrecio()
    elif opcion == 3:
            modificarProducto()
    else:
        main()


# funcion para modificar el precio de algun producto
def modificarPrecio():
    controlBaseDatos.mostrarMenu(dbProductos)
    modificar = int(input("Ingrese el ID del Producto que desea modificar\n"))-1
    # se confirma con el administrador el producto a modificar
    print("Se Modificara el precio de ", dbProductos[modificar])
    nuevoPrecio = input("Ingrese el nuevo precio del producto\n")
    dbProductos[modificar][2] = nuevoPrecio
    # se muestran los cambios realizados
    print("El nuevo producto es ", dbProductos[modificar])
    modificarProducto()


# funcion para modificar el nombre de algun producto
def modificarNombre():
    controlBaseDatos.mostrarMenu(dbProductos)
    modificar = int(input("Ingrese el ID del Producto que desea modificar\n"))-1
    # se confirma con el administrador el producto a modificar
    print("Se Modificara el nombre de ", dbProductos[modificar])
    nuevoNombre = input("Ingrese el nuevo nombre del producto\n")
    dbProductos[modificar][1] = nuevoNombre
    # se muestran los cambios realizados
    print("El nuevo producto es ", dbProductos[modificar])
    modificarProducto()


# funcion para agregar nuevos productos a la base de datos
def agregarProducto():
    controlBaseDatos.mostrarMenu(dbProductos)
    opcion = int(input("""Opciones Disponibles:
    1. Nuevo Producto
    2. Volver al Menu Principal\n"""))
    while opcion == 1:
        nombreProducto = input("Ingresar el nombre del nuevo producto\n")
        precioProducto = input("Ingresar el precio del nuevo producto\n")
        id = len(dbProductos)+1
        # se agrega el producto a la base de datos
        nuevoProducto = [id, nombreProducto, precioProducto]
        dbProductos.append(nuevoProducto)
        opcion = int(input("Desea agregar otro producto? 1 = 'SI' o 2 = 'NO'\n"))
    modificarMenu()


# funcion para eliminar los productos de la base de datos
def eliminarProducto():
    controlBaseDatos.mostrarMenu(dbProductos)
    opcion = int(input("""Opciones Disponibles:
     1. Eliminar Producto
     2. Volver al Menu Principal\n"""))
    if opcion == 1:
        eliminado = int(input("Escriba el ID del producto que desea eliminar\n"))-1
        # se confirma con el administraodr si desea eliminar el producto seleccionado
        confirmacion = int(input("Desea eliminar el producto? 1 = SI o 2 = NO\n"))
        if confirmacion == 1:
            del dbProductos[eliminado]
            for eliminado in range(len(dbProductos)):
                dbProductos[eliminado][0] = eliminado
        # se pregunta si se desea regresar el menu o eliminar otro producto.
        regresar = int(input("Desea regresar al menu principal? 1 = SI o 2 = NO\n"))
        if regresar == 1:
            main()
        else:
            eliminarProducto()
    else:
        modificarMenu()


# funcion para notificar a los usuarios (aun por correo electronico)
def notificarUsuario():
    controlBaseDatos.mostrarUsuarios(dbUsuarios)
    usuario = int(input("ID del usuario a Notificar:\n"))-1
    opcion = int(input("""\nOpciones Disponibles:
    1. Orden Lista
    2. Cambio/Cancelacion de Orden
    3. Regresar al Menu Principal\n"""))
    if opcion == 1:
            ordenLista(usuario)
    elif opcion == 2:
            cambioOrden(usuario)
    else:
        main()


def bangarang():
    controlBaseDatos.mostrarUsuarios(dbUsuarios)
    bannear = int(input("Ingrese ID del usuario a Bannear\n"))-1
    # confirmacion
    confirmacion = int(input("Desea Bannear al usuario {}?  1 = SI , 2 = NO".format(dbUsuarios[bannear])))
    if confirmacion == 1:
        dbUsuarios[bannear][4] = 1
        controlBaseDatos.mostrarUsuarios(dbUsuarios)
        controlBaseDatos.mandarUsuarios(dbUsuarios)
    else:
        main()
    main()


# funcion pendiente orden lista
def ordenLista(usuario):
    mensaje = "Su orden ya esta lista, favor de ir a recogerla a la cafeteria!"
    dbHistorial[usuario][3] = 1
    print(mensaje)


# funcion pendiente cambio o eliminacion de orden
def cambioOrden(usuario):
    motivo = input("Ingrese el Motivo de el cambio o cancelación de la orden:\n")
    dbHistorial[usuario][4] = motivo
    print(motivo)
