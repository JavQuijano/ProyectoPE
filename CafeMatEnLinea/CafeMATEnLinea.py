import iniciarSesion
import registroUsuario
import controlUsuario
import controlAdministrador
import sys
import sqlite3
connCafe = sqlite3.connect("CafeMAT.db")
cursorCafe = connCafe.cursor()


def main():
    bandera = 0
    opcion = int(input("""Bienvenido a CafeMATEnLinea
    Opciones Disponibles:
    1. Iniciar Sesion
    2. Crear Nueva Cuenta
    3. Cerrar Programa\n"""))
    while bandera != 1:
        if opcion == 1:
            correo = input('Ingresar su correo electronico: ')
            contraseña = input('Ingresar su contraseña: ')
            identificador = iniciarSesion.main(correo, contraseña)
            if identificador == (1,):
                controlAdministrador.main()
            elif identificador == "falso":
                sys.exit()
            else:
                controlUsuario.main()
        elif opcion == 2:
            registroUsuario.main()
            sys.exit()
        else:
            print("Hasta Luego, Muchas Gracias!!!")
            cursorCafe.close()
            connCafe.close()
            sys.exit()


main()
