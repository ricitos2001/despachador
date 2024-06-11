# BUSCADOR DE HASHES
consiste en un programa que utiliza un hash para localizar una contraseña

## FUNCIONAMIENTO:
1. ejecutamos el programa de python poniendo la ruta del archivo
ejemplo: python3.12.exe "e:/programacion web/asignaturas/sistemas informaticos/tema 1/actividad 10/gestor_de_procesos.py"
2. el programa verifica si la version de python y en el caso contrario te mostrara un mensaje diciendo que la version no es compatible y que version debes instalar
3. el programa verifica si las librerias necesarias estan instaladas y en el caso contrario mostrara un mensaje de error indicando que librerias no esta instaladas y debes instalar
4. el programa muestra su portada
5. presionamos intro para iniciar el programa
6. el programa obtiene una serie de dato relaccionados con una serie de cuatro grupos con cinco procesos que hay en el archivo de entrada "procesos.txt"
8. cada grupo de procesos pasara por un algoritmo diferente
9. una vez finalizado el proceso el programa mostrara un mensaje diciendo que los datos han sido importados en un archivo de salida llamado "salida.txt" y dichos datos estaran mostrados en una tabla
10. el resultado se mostrara en formato de tabla:
╔═════════════════════╦══════════════╦══════════════╦══════════════╦══════════════╗
║                     ║     FCFS     ║     SJF      ║     SRTF     ║ ROUND ROBIN  ║
╠═════════════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
║ tiempo de espera    ║              ║              ║              ║              ║
╠═════════════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
║ tiempo de retorno   ║              ║              ║              ║              ║
╠═════════════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
║ tiempo de respuesta ║              ║              ║              ║              ║
╠═════════════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
║ uso de la CPU       ║              ║              ║              ║              ║
╠═════════════════════╬══════════════╬══════════════╬══════════════╬══════════════╣
║ productividad       ║              ║              ║              ║              ║
╚═════════════════════╩══════════════╩══════════════╩══════════════╩══════════════╝
## LIBRERIAS A UTILIZAR
1. libreria os
2. libreria sys
3. libreria ast
4. libreria importlib

## PUNTOS A DESTACAR:
1. el programa posee un script para pausar la consola y otro script para limpiar el terminal. Ambos scripts se ejecuta por cada paso del funcionamiento del programa
2. el programa utiliza un archivo de entrada de datos llamado "procesos.txt" y uno de salida llamado "salida.txt"
3. el programa utilizara cuatro grupos de procesos y cada uno servira para un algoritmo en especifico
5. el resultado varia en funcion de las caracteristicas de los procesos