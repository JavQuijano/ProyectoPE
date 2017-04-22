import sqlite3

connUsuarios = sqlite3.connect('usuariosbd.db')
cursor = connUsuarios.cursor()

def main():
    correo = input('Ingresar su correo electronico: ')
    contraseña = input('Ingresar su contraseña: ')
    verificarBaseDatos(correo, contraseña)
    # cerramos conexiones con las bases de datos
    cursor.close()
    connUsuarios.close()



def verificarBaseDatos(correo, contraseña):
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (correo,))
    data = cursor.fetchall()
    contraseña = [(contraseña,)]
    bandera = 0
    while bandera != 1:
        if data != []:
            cursor.execute("SELECT contraseña FROM usuarios WHERE email = ?", (correo,))
            passw = cursor.fetchall()
        else:
            print('El correo electronico no esta registrado, favor de crear una cuenta.')
            break
        if contraseña == passw:
            print('Acceso correcto')
            bandera = 1
        else:
            print('la contraseña no corresponde con el correo, favor de ingresarla nuevamente.')
            contraseña = input('Ingrese su contraseña: ')
            contraseña = [(contraseña,)]

main()
