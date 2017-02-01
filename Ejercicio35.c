//Autor: Damian Moreno Mireles
	//Entradas: Contadores, Tamaño de la tabla
	//Salidas: Valores de la parte superior de la diagonal de la tabla
	//El programa imprime las posiciones de una tabla de tamaño n=> entero positivo
#include <stdio.h>
int main(int argc, char *argv[]) {
	//Definicion y lectura de variables
	int contador1, contador2,contadorDeEspacios = 0, n;
	printf("Introduce la resolucion de la tabla\n");
		scanf("%d",&n);
	//Salida de los valores de la tabla que estan
	//por encima de la diagonal superior
	for(contador1 = 0; contador1 < n; contador1++)
	{
		//este ciclo genera espacios entre las columnas
		printf("\n");
		contadorDeEspacios = 0;
		for(contador2 = contador1; contador2 < n; contador2++)
		{
			//el ciclo while genera espacios en blaco para el ordenamiento de la tabla
			while(contadorDeEspacios < contador1)
			{
				printf("\t");
				contadorDeEspacios++;
			}
			//La salida de los datos correspondientes al espacio
			printf("%d%d\t",contador1,contador2);
		}
	}
	return 0;
	/* comentarios QA:
	La ejecucion es correcta y la sintaxis y/o uso de simbolos tambien solo falto indicar que se esta haciendo cuando el programa se encuentra en ejecucion
	Reviso: Juan Duran*/
}