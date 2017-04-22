import sqlite3

connUsuarios = sqlite3.connect('usuariosbd.db')
cursorUsuarios = connUsuarios.cursor()
connProductos = sqlite3.connect('productosbd.db')
cursorProductos = connProductos.cursor()

def main():
    opcion = int(input("""Bienvenido Administrador
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
        notificarUsario()
    else:
        print("Hasta luego!")


def eliminarUsuarios():
    cursorUsuarios.execute("SELECT * FROM usuarios")
    print("ID, Nombre, E-Mail, Contraseña")
    for linea in cursorUsuarios.fetchall():
        print(linea)
    eliminado = int(input("Escriba el ID del usuario que desea eliminar\n"))
    cursorUsuarios.execute("SELECT * FROM usuarios WHERE ID = ?", (eliminado,))
    usuario = cursorUsuarios.fetchall()
    confirmacion = input("Desea eliminar a {}? 'SI' o 'NO'\n".format(usuario))
    confirmarEliminacion(confirmacion, eliminado)


def confirmarEliminacion(confirmacion, eliminado):
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
    cursorProductos.execute("SELECT * FROM productos")
    print('(ID, PRODUCTO, PRECIO)')
    for producto in cursorProductos.fetchall():
        print(producto)
    modificar = int(input("Ingrese el ID del Producto que desea modificar\n"))
    opcion = int(input("""¿Que Desea Modificar?
    Opciones Disponibles
    1. Modificar Nombre
    2. Modificar Precio
    3. Elegir otro producto
    4. Regresar al Menu Principal\n"""))
    if opcion == 1:
        cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
        productoAModificar = cursorProductos.fetchall()
        print("Se Modificara {}".format(productoAModificar))
        nuevoNombre = input("Ingrese el nuevo nombre del producto\n")
        cursorProductos.execute("UPDATE productos SET producto = ? WHERE ID = ?", (nuevoNombre, modificar,))
        connProductos.commit()
        cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
        productoAModificar = cursorProductos.fetchall()
        print("El nuevo producto es {}".format(productoAModificar))
    elif opcion == 2:
        cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
        productoAModificar = cursorProductos.fetchall()
        print("Se Modificara {}".format(productoAModificar))
        nuevoPrecio = input("Ingrese el nuevo precio del producto\n")
        cursorProductos.execute("UPDATE productos SET precio = ? WHERE ID = ?", (nuevoPrecio, modificar,))
        connProductos.commit()
        cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (modificar,))
        productoAModificar = cursorProductos.fetchall()
        print("El nuevo producto es {}".format(productoAModificar))
    elif opcion == 3:
        modificarProducto()
    else:
        main()


def agregarProducto():
    cursorProductos.execute("SELECT * FROM productos")
    print(""""MENU ACTUAL
    (ID, PRODUCTO, PRECIO)""")
    for producto in cursorProductos.fetchall():
        print(producto)
    opcion = int(input("""Opciones Disponibles:
    1. Nuevo Producto
    2. Volver al Menu Principal\n"""))
    if opcion == 1:
        nombreProducto = input("Ingresar el nombre del nuevo producto\n")
        precioProducto = input("Ingresar el precio del nuevo producto\n")
        cursorProductos.execute("""INSERT INTO productos(producto, precio) VALUES
            (?, ?)""", (nombreProducto, precioProducto))
        connUsuarios.commit()
    else:
        main()


def eliminarProducto():
    cursorProductos.execute("SELECT * FROM productos")
    print(""""MENU ACTUAL
       (ID, PRODUCTO, PRECIO)""")
    for producto in cursorProductos.fetchall():
        print(producto)
    opcion = int(input("""Opciones Disponibles:
     1. Eliminar Producto
     2. Volver al Menu Principal\n"""))
    if opcion == 1:
        eliminado = int(input("Escriba el ID del producto que desea eliminar\n"))
        cursorProductos.execute("SELECT * FROM productos WHERE ID = ?", (eliminado,))
        producto = cursorProductos.fetchall()
        confirmacion = input("Desea eliminar a {}? 'SI' o 'NO'\n".format(producto))
        if confirmacion == "SI":
            cursorProductos.execute("DELETE FROM productos WHERE ID = ?", (eliminado,))
            connProductos.commit()
        regresar = input("Desea regresar al menu principal? 'SI' o 'NO'\n")
        if regresar == 'SI':
            main()
        else:
            eliminarProducto()
    else:
        main()

main()
