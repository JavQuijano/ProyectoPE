import sqlite3
connUsuarios = sqlite3.connect('usuariosbd.db')
cursor = connUsuarios.cursor()

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
    agregarABaseUsuarios(nombreCompleto, emailFinal, contraseñaFinal)
    # Cerramos conexiones con las bases de datos.
    cursor.close()
    connUsuarios.close()


# Esta funcion verifica la validez del correo, al igual que checa si hay otro igual en la base de datos.
def verificarUsuario(email, verEmail):
    bandera = 0
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
    correo = cursor.fetchall()
    # Ciclo en el cual se analiza la validez del correo
    while bandera != 1:
        if email == verEmail:
            bandera = 1
            if correo == []:
                bandera = 1
            else:
                print('El correo que ingreso ya existe, ingrese su correo nuevamente.')
                email = input('Ingrese su email: ')
                verEmail = input('Vuelva a ingresar su email: ')
        else:
            print('ingrese nuevamente el correo electronico')
            email = input('Ingrese su email: ')
            verEmail = input('Vuelva a ingresar su email: ')
    print('Correo electronico correcto')
    emailFinal = email
    return emailFinal


def verificarContraseña(contraseña, verContraseña):
    bandera = 0
    while bandera != 1:
        if contraseña == verContraseña:
            bandera = 1
        else:
            print('Ingrese nuevamente la contraseña')
            contraseña = input('Ingrese su contraseña: ')
            verContraseña = input('Vuelva a ingresar su contraseña: ')
    print('Contraseña correcta')
    contraseñaFinal = contraseña
    return contraseñaFinal


def agregarABaseUsuarios(nombreCompleto, emailFinal, contraseñaFinal):
    cursor.execute("""INSERT INTO usuarios(nombre, email, contraseña) VALUES
    (?, ?, ?)""", (nombreCompleto, emailFinal, contraseñaFinal))
    connUsuarios.commit()


main()
