import sqlite3

connUsuarios = sqlite3.connect('usuariosbd.db')
cursorUsuarios = connUsuarios.cursor()
connProductos = sqlite3.connect('productosbd.db')
cursorProductos = connProductos.cursor()


def main():
    opcion = int(input("""  Bienvenido Administrador
    Seleccione la opcion deseada:
    1. Eliminar Usuario
    2. Modificar Menu
    3. Notificar Usuario
    4. Cerrar Programa\n"""))
    if opcion == 1:
        eliminarUsuarios()
    elif opcion == 2:
        modificarMenu()
    elif opcion == 3:
        notificarUsuario()
    else:
        cursorProductos.close()
        connProductos.close()
        cursorUsuarios.close()
        connUsuarios.close()
        print("Adios Administrador!")


def eliminarUsuarios():
    mostrarUsuarios()
    eliminado = int(input("Escriba el ID del usuario que desea eliminar\n"))
    cursorUsuarios.execute("SELECT * FROM usuarios WHERE ID = ?", (eliminado,))
    usuario = cursorUsuarios.fetchall()
    confirmacion = input("Desea eliminar a {}? 'SI' o 'NO'\n".format(usuario))
    if confirmacion == 'SI':
        cursorUsuarios.execute("DELETE FROM usuarios WHERE ID = ?", (eliminado,))
        connUsuarios.commit()
        regresar = input("Desea regresar al menu principal? 'SI' o 'NO'\n")
        if regresar == 'SI':
            main()
        else:
            eliminarUsuarios()
    else:
        regresar = input("Desea regresar al menu principal? 'SI' o 'NO'\n")
        if regresar == 'SI':
            main()
        else:
            eliminarUsuarios()


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


def modificarPrecio():
    mostrarMenu()
    modificar = int(input("Ingrese el ID del Producto que desea modificar\n"))
    cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
    productoAModificar = cursorProductos.fetchall()
    print("Se Modificara el precio de {}".format(productoAModificar))
    nuevoPrecio = input("Ingrese el nuevo precio del producto\n")
    cursorProductos.execute("UPDATE productos SET precio = ? WHERE ID = ?", (nuevoPrecio, modificar,))
    connProductos.commit()
    cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
    productoAModificar = cursorProductos.fetchall()
    print("El nuevo producto es {}".format(productoAModificar))
    modificarProducto()


def modificarNombre():
    mostrarMenu()
    modificar = int(input("Ingrese el ID del Producto que desea modificar\n"))
    cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
    productoAModificar = cursorProductos.fetchall()
    print("Se Modificara el nombre de {}".format(productoAModificar))
    nuevoNombre = input("Ingrese el nuevo nombre del producto\n")
    cursorProductos.execute("UPDATE productos SET producto = ? WHERE ID = ?", (nuevoNombre, modificar,))
    connProductos.commit()
    cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
    productoAModificar = cursorProductos.fetchall()
    print("El nuevo producto es {}".format(productoAModificar))
    modificarProducto()


def agregarProducto():
    mostrarMenu()
    opcion = int(input("""Opciones Disponibles:
    1. Nuevo Producto
    2. Volver al Menu Principal\n"""))
    while opcion == 1:
        nombreProducto = input("Ingresar el nombre del nuevo producto\n")
        precioProducto = input("Ingresar el precio del nuevo producto\n")
        cursorProductos.execute("""INSERT INTO productos(producto, precio) VALUES
            (?, ?)""", (nombreProducto, precioProducto))
        connUsuarios.commit()
        opcion = int(input("Desea agregar otro producto? 1 = 'SI' o 2 = 'NO'\n"))
    modificarMenu()


def eliminarProducto():
    mostrarMenu()
    opcion = int(input("""Opciones Disponibles:
     1. Eliminar Producto
     2. Volver al Menu Principal\n"""))
    if opcion == 1:
        eliminado = int(input("Escriba el ID del producto que desea eliminar\n"))
        cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (eliminado,))
        producto = cursorProductos.fetchall()
        confirmacion = int(input("Desea eliminar a {}? 1 = SI o 2 = NO\n".format(producto)))
        if confirmacion == 1:
            cursorProductos.execute("DELETE FROM productos WHERE ID = ?", (eliminado,))
            connProductos.commit()
        regresar = int(input("Desea regresar al menu principal? 1 = SI o 2 = NO\n"))
        if regresar == 1:
            main()
        else:
            eliminarProducto()
    else:
        modificarMenu()


def notificarUsuario():
    mostrarUsuarios()
    usuario = int(input("ID del usuario a Notificar:\n"))
    cursorUsuarios.execute("SELECT email FROM usuarios WHERE id = ?", (usuario,))
    correo = cursorUsuarios.fetchone()
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


def ordenLista(correo):
    mensaje = "Su orden ya esta lista, favor de ir a recogerla a la cafeteria!"
    # Aqui va la notificacion por correo enviar variable "mensaje".


def cambioOrden(correo):
    motivo = input("Ingrese el Motivo de el cambio o cancelación de la orden:\n")
    # Aqui va la notificacion por correo enviar variable "motivo".


def mostrarMenu():
    cursorProductos.execute("SELECT * FROM productos")
    print(""""MENU ACTUAL
(ID, PRODUCTO, PRECIO)""")
    for producto in cursorProductos.fetchall():
        print(producto)


def mostrarUsuarios():
    cursorUsuarios.execute("SELECT * FROM usuarios")
    print("ID, Nombre, E-Mail, Contraseña")
    for linea in cursorUsuarios.fetchall():
        print(linea)
