# modulo para el manejo de base de datos
import controlBaseDatos
import sqlite3
# coneccion con la base de datos
connCafe = sqlite3.connect('CafeMAT.db')
cursorCafe = connCafe.cursor()
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
5. Cerrar Programa\n"""))
    if opcion == 1:
        eliminarUsuarios()
    elif opcion == 2:
        modificarMenu()
    elif opcion == 3:
        notificarUsuario()
    elif opcion == 4:
        consultarOrdenes()
        main()
    else:
        print("Adios Administrador!")
        import CafeMATEnLinea
        CafeMATEnLinea.main()


# funcion para la eliminacion de usuarios
def eliminarUsuarios():
    mostrarUsuarios()
    eliminado = int(input("Escriba el ID del usuario que desea eliminar\n"))
    cursorCafe.execute("SELECT * FROM usuarios WHERE id = ?", (eliminado,))
    usuario = cursorCafe.fetchall()
    # confirma si se desea eliminar al usuario seleccionado
    confirmacion = input("Desea eliminar a {}? '1 = SI' o '2 = NO'\n".format(usuario))
    if confirmacion == '1':
        cursorCafe.execute("DELETE FROM usuarios WHERE id = ?", (eliminado,))
        connCafe.commit()
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
    mostrarMenu()
    modificar = int(input("Ingrese el ID del Producto que desea modificar\n"))
    cursorCafe.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
    productoAModificar = cursorCafe.fetchall()
    # se confirma con el administrador el producto a modificar
    print("Se Modificara el precio de {}".format(productoAModificar))
    nuevoPrecio = input("Ingrese el nuevo precio del producto\n")
    cursorCafe.execute("UPDATE productos SET precio = ? WHERE ID = ?", (nuevoPrecio, modificar,))
    connCafe.commit()
    cursorCafe.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
    productoAModificar = cursorCafe.fetchall()
    # se muestran los cambios realizados
    print("El nuevo producto es {}".format(productoAModificar))
    modificarProducto()


# funcion para modificar el nombre de algun producto
def modificarNombre():
    mostrarMenu()
    modificar = int(input("Ingrese el ID del Producto que desea modificar\n"))
    cursorCafe.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
    productoAModificar = cursorCafe.fetchall()
    # se confirma con el administrador el producto a modificar
    print("Se Modificara el nombre de {}".format(productoAModificar))
    nuevoNombre = input("Ingrese el nuevo nombre del producto\n")
    cursorCafe.execute("UPDATE productos SET producto = ? WHERE ID = ?", (nuevoNombre, modificar,))
    connCafe.commit()
    cursorCafe.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
    productoAModificar = cursorCafe.fetchall()
    # se muestran los cambios realizados
    print("El nuevo producto es {}".format(productoAModificar))
    modificarProducto()


# funcion para agregar nuevos productos a la base de datos
def agregarProducto():
    mostrarMenu()
    opcion = int(input("""Opciones Disponibles:
    1. Nuevo Producto
    2. Volver al Menu Principal\n"""))
    while opcion == 1:
        nombreProducto = input("Ingresar el nombre del nuevo producto\n")
        precioProducto = input("Ingresar el precio del nuevo producto\n")
        # se agrega el producto a la base de datos
        cursorCafe.execute("""INSERT INTO productos(producto, precio) VALUES
            (?, ?)""", (nombreProducto, precioProducto))
        connCafe.commit()
        opcion = int(input("Desea agregar otro producto? 1 = 'SI' o 2 = 'NO'\n"))
    modificarMenu()


# funcion para eliminar los productos de la base de datos
def eliminarProducto():
    mostrarMenu()
    opcion = int(input("""Opciones Disponibles:
     1. Eliminar Producto
     2. Volver al Menu Principal\n"""))
    if opcion == 1:
        eliminado = int(input("Escriba el ID del producto que desea eliminar\n"))
        cursorCafe.execute("SELECT * FROM productos WHERE ID = ?", (eliminado,))
        producto = cursorCafe.fetchall()
        # se confirma con el administraodr si desea eliminar el producto seleccionado
        confirmacion = int(input("Desea eliminar a {}? 1 = SI o 2 = NO\n".format(producto)))
        if confirmacion == 1:
            cursorCafe.execute("DELETE FROM productos WHERE ID = ?", (eliminado,))
            connCafe.commit()
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
    mostrarUsuarios()
    usuario = int(input("ID del usuario a Notificar:\n"))
    cursorCafe.execute("SELECT email FROM usuarios WHERE id = ?", (usuario,))
    correo = cursorCafe.fetchone()
    opcion = int(input("""\nOpciones Disponibles:
    1. Orden Lista
    2. Cambio/Cancelacion de Orden
    3. Regresar al Menu Principal\n"""))
    if opcion == 1:
            ordenLista(correo)
    elif opcion == 2:
            cambioOrden(correo)
    else:
        main()


# funcion pendiente orden lista
def ordenLista(correo):
    mensaje = "Su orden ya esta lista, favor de ir a recogerla a la cafeteria!"
    # Aqui va la notificacion por correo enviar variable "mensaje".


# funcion pendiente cambio o eliminacion de orden
def cambioOrden(correo):
    motivo = input("Ingrese el Motivo de el cambio o cancelación de la orden:\n")
    # Aqui va la notificacion por correo enviar variable "motivo".


# muestra el menu de productos actual
def mostrarMenu():
    print(""""MENU ACTUAL
(ID, PRODUCTO, PRECIO)""")
    for producto in dbProductos:
        print(producto)


# muestra la lista de usuarios registrados
def mostrarUsuarios():
    print("ID, Nombre, E-Mail, Contraseña")
    for linea in dbUsuarios:
        print(linea)


def consultarOrdenes():
    print("ID, Productos, Precio, Entregado?")
    for i in dbHistorial:
        print(i)
