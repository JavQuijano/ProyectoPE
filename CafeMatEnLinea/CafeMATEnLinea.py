import iniciarSesion
import registroUsuario
import controlUsuario
import controlAdministrador


def main():
    opcion = int(input(""" Bienvenido a CafeMATEnLinea
    Opciones Disponibles:
    1. Iniciar Sesion
    2. Crear Nueva Cuenta
    3. Cerrar Programa\n"""))

    bandera = 0
    while bandera != 1:
        if opcion == 1:
            correo = input('Ingresar su correo electronico: ')
            contraseña = input('Ingresar su contraseña: ')
            identificador = iniciarSesion.main(correo, contraseña)
            if identificador == (1,):
                controlAdministrador.main()
                bandera = 1
            else:
                controlUsuario.main()
                bandera = 1
        elif opcion == 2:
            registroUsuario.main()
            bandera = 1
        else:
            bandera = 1
    print("Hasta Luego, Muchas Gracias!!!")


main()
