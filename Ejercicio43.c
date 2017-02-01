/*
Autor:Francisco Quijano 30/Enero/17
Entradas: datos numericos a analizar.
Salidas: cantidad de numeros positivos y negativos.
Procedimiento general:
se analizaran los datos leidos y se contara el numero
de datos positivos y negativos.
*/
#include <stdio.h>
int main(int argc, char *argv[]) {
	/*Definición de variables*/
  float variable = 1;
  int positivos = 0;
  int negativos = 0;
  /*Entradas*/
  /*en este bloque se leen y analizan los valores introducidos por
  el usuario*/
  printf("introduzca los valores para analizar, marque el final con un 0\n");
  while (variable != 0){
    scanf("%f", &variable);
    if (variable > 0){
      positivos++;
    }
    else{
      negativos++;
    }
  }
  /*aqui se sustrae el "0" que fue conciderado como negativo*/
  negativos--;
  /*Salidas*/
  printf("El total de positivos es: %d\nEl total de negativos es: %d", positivos, negativos);
  return 0;
}
/*Notas de QA

QA: Luis Madera
El programa cumple con el procedimiento definido donde debe analizar su un numero es positivo o negativo, se introducen 3 casos prueba, cumpliendo con su función.
Esta estructurado de la forma preestablecida contando con nombre de autor y las etapas correspondientes.
*/
