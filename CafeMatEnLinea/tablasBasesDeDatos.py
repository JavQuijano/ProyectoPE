# importamos el modulo para el manejo de bases de datos
import sqlite3
# iniciamos la coneccion con la base de datos
connCafe = sqlite3.connect('CafeMAT.db')
cursorCafe = connCafe.cursor()


# funcion principal para crear las diferentes tablas
def main():
    tablaUsuarios()
    tablaProductos()
    tablaHistorial()
    print("Las Tablas se crearon con Exito!")
    # cerramos conexiones con las bases de datos
    cursorCafe.close()
    connCafe.close()


# creacion de la tabla usuarios
def tablaUsuarios():
    try:
        cursorCafe.execute("""CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nombre TEXT NOT NULL,
        email TEXT NOT NULL,
        contraseña TEXT NOT NULL,
        bandera INTEGER NOT NULL)
        """)
        connCafe.commit()
    except sqlite3.OperationalError:
        print('la tabla usuarios no se creo correctamente')


# creacion de la tabla productos
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


# creacion de la tabla historial de productos
def tablaHistorial():
    try:
        cursorCafe.execute("""CREATE TABLE IF NOT EXISTS historial(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        pedido TEXT NOT NULL,
        total REAL NOT NULL,
        entregada INTEGER NOT NULL)""")
        connCafe.commit()
    except sqlite3.OperationalError:
        print("la tabla historial no fue creada correctamente")


main()
