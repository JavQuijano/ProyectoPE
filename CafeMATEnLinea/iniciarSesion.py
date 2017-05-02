# modulo de coneccion a base de datos
import sqlite3
# iniciar coneccion con la base de datos
connCafe = sqlite3.connect('CafeMAT.db')
cursorCafe = connCafe.cursor()


# funcion que devuelve el identificador del usuario
def main(correo, contraseña):
    identificador = verificarBaseDatos(correo, contraseña)
    return identificador


# verifica que el correo y la contraseña existan en la base de datos
def verificarBaseDatos(correo, contraseña):
    identificador = 0
    # selecciona la informacion del usuario dentro de la base de datos
    cursorCafe.execute("SELECT * FROM usuarios WHERE email = ?", (correo,))
    data = cursorCafe.fetchall()
    # le da el formato que coincide con el de la base datos para poder verificar
    contraseña = [(contraseña,)]
    bandera = 0
    # mientras no se cumplan las condiciones el programa requerira que la informacion
    # se vuelva a introducir
    while bandera != 1:
        # si el usuario no se encuentra registrado, le pedira que se registre y vuelve al menu principal
        if data != []:
            cursorCafe.execute("SELECT contraseña FROM usuarios WHERE email = ?", (correo,))
            passw = cursorCafe.fetchall()
        else:
            print('El correo electronico no esta registrado, favor de crear una cuenta.')
            identificador = "falso"
            break
        # si la contraseña no corresponde con el correo, le pide al usuario que la ingrese nuevamente
        if contraseña == passw:
            print('Acceso correcto')
            cursorCafe.execute("SELECT id FROM usuarios WHERE email = ?", (correo,))
            identificador = cursorCafe.fetchone()
            bandera = 1
        else:
            print('la contraseña no corresponde con el correo, favor de ingresarla nuevamente.')
            contraseña = input('Ingrese su contraseña: ')
            contraseña = [(contraseña,)]
    # regresa el identificador a la funcion main
    return identificador
