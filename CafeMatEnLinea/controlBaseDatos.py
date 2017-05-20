import sqlite3
connCafe = sqlite3.connect("CafeMAT.db")
cursorCafe = connCafe.cursor()


# funciones tabla productos
def agregarProducto(nombreProducto, precioProducto):
    cursorCafe.execute("""INSERT INTO productos (producto, precio)
    VALUES (?, ?)""", (nombreProducto, precioProducto))
    connCafe.commit()


def eliminarProducto(identificador):
    cursorCafe.execute("""DELETE FROM productos
    WHERE id = ?""", (identificador,))
    connCafe.commit()


def modificarPrecio(identificador, nuevoPrecio):
    cursorCafe.execute("""UPDATE productos SET precio = ?
    WHERE id = ?""", (nuevoPrecio, identificador))
    connCafe.commit()


def modificarNombre(identificador, nuevoNombre):
    cursorCafe.execute("""UPDATE productos SET producto = ?
    WHERE id = ?""", (nuevoNombre, identificador))
    connCafe.commit()


# funciones tabla usuarios
def agregarUsuario(nombre, email, contraseña):
    cursorCafe.execute("""INSERT INTO usuarios (nombre, email, contraseña)
    VALUES (?, ?, ?)""", (nombre, email, contraseña))
    connCafe.commit()


def eliminarUsuario(identificador):
    cursorCafe.execute("""DELETE FROM usuarios
    WHERE id = ?""", (identificador,))
    connCafe.commit()


# funciones imprimir tablas
def imprimirMenu():
    cursorCafe.execute("SELECT * FROM productos")
    print(""""MENU ACTUAL
(ID, PRODUCTO, PRECIO)""")
    for producto in cursorCafe.fetchall():
        print(producto)


def imprimirUsuarios():
    cursorCafe.execute("SELECT * FROM usuarios")
    print("ID, Nombre, E-Mail, Contraseña")
    for usuario in cursorCafe.fetchall():
        print(usuario)


def imprimirOrdenes():
    cursorCafe.execute("SELECT * FROM ordenes")
    print("ID, Productos, Precio")
    for orden in cursorCafe.fetchall():
        print(orden)


#A partir de aqui, se carga la base de datos en la memoria para realizar las busquedas y modificaciones.


def iniciarUsuarios():
    listaUsuarios = []
    cursorCafe.execute("SELECT * FROM usuarios")
    usuarios = list(cursorCafe.fetchall())
    totalUsuarios = len(usuarios)
    for i in range(totalUsuarios):
        listaUsuarios.append(usuarios[i])
    return listaUsuarios



def iniciarProductos():
    listaProductos = []
    cursorCafe.execute("SELECT * FROM usuarios")
    productos = list(cursorCafe.fetchall())
    totalProductos = len(productos)
    for i in range(totalProductos):
        listaProductos.append(productos[i])
    return listaProductos


def iniciarHistorial():
    listaHistorial = []
    cursorCafe.execute("SELECT * FROM usuarios")
    historial = list(cursorCafe.fetchall())
    totalHistorial = len(historial)
    for i in range(totalHistorial):
        listaHistorial.append(historial[i])
    return listaHistorial


def buscarUsuario(email):
    listaUsuarios = iniciarUsuarios()
    usuario = []
    for i in range(len(listaUsuarios)):
        listaEmail = listaUsuarios[i]
        listaEmail = listaEmail[2]
        if email == listaEmail:
                usuario = listaUsuarios[i]
    return usuario
