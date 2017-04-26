import sqlite3
connUsuarios = sqlite3.connect('usuariosbd.db')
cursorUsuarios = connUsuarios.cursor()
connProductos = sqlite3.connect('productosbd.db')
cursorProductos = connProductos.cursor()


def main():
    tablaUsuarios()
    tablaProductos()
    # cerramos conexiones con las bases de datos
    cursorUsuarios.close()
    connUsuarios.close()
    cursorProductos.close()
    connProductos.close()


def tablaUsuarios():
    try:
        cursorUsuarios.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        contraseña TEXT NOT NULL)
        """)
        connUsuarios.commit()
    except sqlite3.OperationalError:
        print('la tabla no se creo correctamente')


def tablaProductos():
    try:
        cursorProductos.execute("""CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        producto TEXT NOT NULL,
        precio REAL NOT NULL)
        """)
    except sqlite3.OperationalError:
        print('la tabla no se creo correctamente')


main()
