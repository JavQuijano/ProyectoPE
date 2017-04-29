import sqlite3
connCafe = sqlite3.connect('CafeMAT.db')
cursorCafe = connCafe.cursor()


def main():
    tablaUsuarios()
    tablaProductos()
    tablaHistorial()
    print("Las Tablas se crearon con Exito!")
    # cerramos conexiones con las bases de datos
    cursorCafe.close()
    connCafe.close()


def tablaUsuarios():
    try:
        cursorCafe.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        contraseña TEXT NOT NULL)
        """)
        connCafe.commit()
    except sqlite3.OperationalError:
        print('la tabla usuarios no se creo correctamente')


def tablaProductos():
    try:
        cursorCafe.execute("""CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        producto TEXT NOT NULL,
        precio REAL NOT NULL)
        """)
        connCafe.commit()
    except sqlite3.OperationalError:
        print('la tabla productos no se creo correctamente')


def tablaHistorial():
    try:
        cursorCafe.execute("""CREATE TABLE IF NOT EXISTS historial(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        pedido TEXT NOT NULL,
        total REAL NOT NULL)""")
        connCafe.commit()
    except sqlite3.OperationalError:
        print("la tabla historial no fue creada correctamente")


main()
