import controlBaseDatos


def verificarBaseDatos(correo, contraseña):
    identificador = 0
    data = controlBaseDatos.buscarUsuario(correo)
    bandera = 0
    while bandera != 1:
        if data != []:
            passw = data[3]
        else:
            print('El correo electronico no esta registrado, favor de crear una cuenta.')
            identificador = "falso"
            break
        if contraseña == passw:
            print('Acceso correcto')
            identificador = data[0]
            bandera = 1
        else:
            print('la contraseña no corresponde con el correo, favor de ingresarla nuevamente.')
            contraseña = input('Ingrese su contraseña: ')
        if data[4] == 0:
            identificador = "bann"
            break
    return identificador
