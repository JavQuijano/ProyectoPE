# importamos los archivos del programa
import iniciarSesion
import registroUsuario
import controlUsuario
import controlAdministrador


# la funcion principal que le dara orden a nuestro programa
def main():
    # menu principal de inicio de sesion
    opcion = int(input("""Bienvenido a CafeMATEnLinea
    Opciones Disponibles:
    1. Iniciar Sesion
    2. Crear Nueva Cuenta
    3. Cerrar Programa\n"""))
    # ejecuta el programa para el inicio de sesion
    if opcion == 1:
        correo = input('Ingresar su correo electronico: ')
        contraseña = input('Ingresar su contraseña: ')
        identificador = iniciarSesion.verificarBaseDatos(correo, contraseña)
        # dependiendo del identificador del usuario ejecutaremos el control del admin o del usuario.
        # por otro lado, si el usuario no esta registrado devolvera falso y cerrara el programa.
        if identificador == 1:
            controlAdministrador.main()
        elif identificador == "falso":
            main()
        elif identificador == "bann":
            print("El usuario esta banneado del sistema.")
            main()
        else:
            controlUsuario.main()
    # ejecuta el programa para registrar a nuevos usuarios
    # al finalizar cierra el programa
    elif opcion == 2:
        registroUsuario.main()
        main()
    # cierra el programa si la opcion es seleccionada
    else:
        print("Hasta Luego, Muchas Gracias!!!")


main()
