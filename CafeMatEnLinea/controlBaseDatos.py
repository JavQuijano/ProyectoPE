import sqlite3
connCafe = sqlite3.connect("CafeMAT.db")
cursorCafe = connCafe.cursor()


# funciones tabla usuarios
def agregarUsuario(nombre, email, contraseña):
    cursorCafe.execute("""INSERT INTO usuarios (nombre, email, contraseña, bandera)
    VALUES (?, ?, ?, 0)""", (nombre, email, contraseña))
    connCafe.commit()


def iniciarUsuarios():
    listaUsuarios = []
    cursorCafe.execute("SELECT * FROM usuarios")
    usuarios = list(cursorCafe.fetchall())
    totalUsuarios = len(usuarios)
    for i in range(totalUsuarios):
        listaUsuarios.append(list(usuarios[i]))
    return listaUsuarios


def iniciarProductos():
    listaProductos = []
    cursorCafe.execute("SELECT * FROM productos")
    productos = list(cursorCafe.fetchall())
    totalProductos = len(productos)
    for i in range(totalProductos):
        listaProductos.append(list(productos[i]))
    return listaProductos


def iniciarHistorial():
    listaHistorial = []
    cursorCafe.execute("SELECT * FROM historial")
    historial = list(cursorCafe.fetchall())
    totalHistorial = len(historial)
    for i in range(totalHistorial):
        listaHistorial.append(list(historial[i]))
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


def buscarIdUsuario(identificador):
    listaUsuarios = iniciarUsuarios()
    usuario = []
    for i in range(len(listaUsuarios)):
        listaEmail = listaUsuarios[i]
        listaEmail = listaEmail[0]
        if identificador == listaEmail:
            usuario = listaUsuarios[i]
    return usuario


def buscarProductos(identificador):
    listaProductos = iniciarProductos()
    producto = []
    for i in range(len(listaProductos)):
        lista = listaProductos[i]
        lista = lista[0]
        if identificador == lista:
            producto = listaProductos[i]
    return producto


def buscarOrdenes(identificador):
    listaHistorial = iniciarHistorial()
    historial = []
    for i in range(len(listaHistorial)):
        lista = listaHistorial[i]
        lista = lista[0]
        if identificador == lista:
            historial = listaHistorial[i]
    return historial


def mandarPedidos(dbHistorial):
    n = 1
    for i in range(len(dbHistorial)):
        cursorCafe.execute("DELETE FROM historial WHERE id = ?", (n,))
        connCafe.commit()
        cursorCafe.execute("""INSERT INTO historial (pedido, total, entregada, motivo)
        VALUES (?, ?, 0, "")""", (dbHistorial[i][1], dbHistorial[i][2]))
        connCafe.commit()
        n += 1


def mandarProductos(dbProductos):
    n = 1
    for i in range(len(dbProductos)):
        cursorCafe.execute("DELETE FROM productos WHERE id = ?", (n,))
        connCafe.commit()
        cursorCafe.execute("""INSERT INTO historial (producto, precio)
        VALUES (?, ?)""", (dbProductos[i][1], dbProductos[i][2]))
        connCafe.commit()
        n += 1


def mandarUsuarios(dbUsuarios):
    n = 1
    for i in range(1, len(dbUsuarios)):
        cursorCafe.execute("DELETE FROM usuarios WHERE id = ?", (n,))
        connCafe.commit()
        cursorCafe.execute("""INSERT INTO usuarios (nombre, email, contraseña, bandera)
            VALUES (?, ?, ?, 0)""", (dbUsuarios[i][1], dbUsuarios[i][2], dbUsuarios[i][3]))
        connCafe.commit()
        n += 1


# muestra el menu de productos actual
def mostrarMenu(dbProductos):
    print(""""MENU ACTUAL
(ID, PRODUCTO, PRECIO)""")
    for producto in dbProductos:
        print(producto)


# muestra la lista de usuarios registrados
def mostrarUsuarios(dbUsuarios):
    print("ID, Nombre, E-Mail, Contraseña")
    for linea in dbUsuarios:
        print(linea)


def consultarOrdenes(dbHistorial):
    print("ID, Productos, Precio, Entregado?")
    for i in dbHistorial:
        print(i)
