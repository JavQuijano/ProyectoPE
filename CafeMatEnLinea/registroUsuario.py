import controlBaseDatos



# funcion main requiere la informacion que se ingresara a la base de datos
def main():
    # Ingresamos la información que queremos ingresar a la base de datos.
    nombreCompleto = input('Ingrese su nombre completo: ')
    email = input('Ingrese su email: ')
    verEmail = input('Vuelva a ingresar su email: ')
    contraseña = input('Ingrese su contraseña: ')
    verContraseña = input('Vuelva a ingresar su contraseña: ')
    # Llamamos a las funciones para verificar la validez del email y contraseña.
    emailFinal = verificarUsuario(email, verEmail)
    contraseñaFinal = verificarContraseña(contraseña, verContraseña)
    # Llamamos a la funcion que ingresara la informacion final a la base de datos.
    controlBaseDatos.agregarUsuario(nombreCompleto, emailFinal, contraseñaFinal)
    import CafeMATEnLinea
    CafeMATEnLinea.main()


# Esta funcion verifica la validez del correo, al igual que checa si hay otro igual en la base de datos.
def verificarUsuario(email, verEmail):
    bandera = 0
    usuario = controlBaseDatos.buscarUsuario(email)
    # Ciclo en el cual se analiza la validez del correo
    while bandera != 1:
        if email == verEmail:
            bandera = 1
            # Se analiza si el correo ya existe dentro de la base de datos.
            if usuario == []:
                bandera = 1
            else:
                print('El correo que ingreso ya existe, ingrese su correo nuevamente.')
                email = input('Ingrese su email: ')
                verEmail = input('Vuelva a ingresar su email: ')
        else:
            print('ingrese nuevamente el correo electronico')
            email = input('Ingrese su email: ')
            verEmail = input('Vuelva a ingresar su email: ')
    # se confirma la validez del correo electronico.
    print('Correo electronico correcto')
    emailFinal = email
    return emailFinal


# funcion que verifica que las 2 veces que se ingreso la contraseña correspondan entre si.
def verificarContraseña(contraseña, verContraseña):
    bandera = 0
    # ciclo para analizar la validez de la contraseña.
    while bandera != 1:
        if contraseña == verContraseña:
            bandera = 1
        else:
            print('Ingrese nuevamente la contraseña')
            contraseña = input('Ingrese su contraseña: ')
            verContraseña = input('Vuelva a ingresar su contraseña: ')
    #se confirma la validez de la contraseña
    print('Contraseña correcta')
    contraseñaFinal = contraseña
    return contraseñaFinal
