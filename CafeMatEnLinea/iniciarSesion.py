import sqlite3

connCafe = sqlite3.connect('CafeMAT.db')
cursorCafe = connCafe.cursor()


def main(correo, contraseña):
    identificador = verificarBaseDatos(correo, contraseña)
    return identificador


def verificarBaseDatos(correo, contraseña):
    identificador = 0
    cursorCafe.execute("SELECT * FROM usuarios WHERE email = ?", (correo,))
    data = cursorCafe.fetchall()
    contraseña = [(contraseña,)]
    bandera = 0
    while bandera != 1:
        if data != []:
            cursorCafe.execute("SELECT contraseña FROM usuarios WHERE email = ?", (correo,))
            passw = cursorCafe.fetchall()
        else:
            print('El correo electronico no esta registrado, favor de crear una cuenta.')
            identificador = "falso"
            break
        if contraseña == passw:
            print('Acceso correcto')
            cursorCafe.execute("SELECT id FROM usuarios WHERE email = ?", (correo,))
            identificador = cursorCafe.fetchone()
            bandera = 1
        else:
            print('la contraseña no corresponde con el correo, favor de ingresarla nuevamente.')
            contraseña = input('Ingrese su contraseña: ')
            contraseña = [(contraseña,)]
    return identificador
