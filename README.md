# DESPACHADOR
consiste en un programa que simula los algoritmos FCFS o FIFO, SJF, SRTF y ROUND ROBIN recibiendo una 
serie de datos de un fichero de entrada llamado "procesos.txt" y mostrando una serie de resultados en un archivo de salida llamado "salida.txt"
Los datos son una serie de veinte procesos dividios en cuantro grupos los cuales a cada uno se les asigna un algoritmo ademas de un valor cuantico o quantum para el algoritmo ROUND ROBIN y los resultados que se muestran son el promedio del tiempo de espera y el promedio del tiempo de retorno de cada algoritmo

## FUNCIONAMIENTO:
1. abrimos un terminal y accedemos al directorio donde esta ubicado el programa 
2. Una vez estemos dentro del directorio ejecutamos el programa de python
3. El programa verifica si la version de python y en el caso contrario te mostrara un mensaje diciendo que la version no es compatible y que version debes instalar
4. El programa verifica si las librerias necesarias estan instaladas y en el caso contrario mostrara un mensaje de error indicando que librerias no esta instaladas y debes instalar
5. El programa muestra su portada
6. presionamos intro para iniciar el proceso ejecucion
7. El programa comprueba si los archivos de entrada y de salida son correctos y si el formato de ambos arhivos es valido o no. En el caso contrario lanzara un mensaje de error y el programa finalizara
8. El programa obtiene una serie de datos relaccionados con una serie de cuatro grupos con cinco procesos que hay en el archivo de entrada "procesos.txt". En el caso de que no haya datos
9. En el caso de que haya datos el programa comprobara si los porcesos siguen el formato adecuado:
P1:0:2 
En el caso de que el formato no sea el adecuado lanzara un mensaje de error y el programa finalizara
10. Cada grupo de procesos pasara por un algoritmo diferente
* El primer grupo pasara por el algoritmo FCFS o FIFO
* El segundo grupo pasara por el algoritmo SJF
* El tercer grupo pasara por el algoritmo SRTF
* El cuarto grupo pasara por el algoritmo ROUND ROBIN
11. Una vez finalizado el proceso el programa mostrara los resultados por pantalla y mostrara un mensaje diciendo que los datos han sido importados en un archivo de salida llamado "salida.txt" entonces el programa finalizara y si nos vamos al archivo de salida veremos que los datos mostrados por el terminal fueron importados. En el caso de que ya haya datos en el archivo se sobreescribiran por los nuevos. El mensaje de salida que indica que los datos fueron importados varia dependiendo de si ya hay datos en el archivo o no

## LIBRERIAS A UTILIZAR
1. libreria os
2. libreria sys
3. libreria ast
4. libreria importlib

## PUNTOS A DESTACAR:
1. el programa posee un script para pausar la consola y otro script para limpiar el terminal. Ambos scripts se ejecuta por cada paso del funcionamiento del programa
2. el programa utiliza un archivo de entrada de datos llamado "procesos.txt" y uno de salida llamado "salida.txt"
3. el programa utilizara cuatro grupos de procesos y cada uno servira para un algoritmo en especifico
4. el resultado varia en funcion de las caracteristicas de los procesos
5. el programa cuenta con una serie de medidas para se cierre en caso de que haya un error en nombre, formato o contenido del archivo de entrada