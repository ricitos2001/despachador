\\CONCEPTOS DE UN ALGORITMO//
- el tiempo de llegada: es el tiempo en el que tarda un proceso en llegar
- tiempo de respuesta: el tiempo de espera de un proceso bloqueado hasta su ejecución
- el tiempo de espera: es el tiempo de espera de un proceso
- tiempo de ejecución: es el tiempo en el que dura la ejecución de un programa
- tiempo de retorno: la suma entre el tiempo de espera y el tiempo de ejecución 

\\CLASES DE ALGORITMOS//
- algoritmos apropiativos: son aquellos algoritmos que no pueden ser expulsados del procesador por otros algoritmos
- algoritmos no apropiativos: son aquellos algoritmos que pueden ser expulsados del procesador por otros algoritmos

\\TIPOS ALGORITMOS//
- FCFS o FIFO (algoritmo por orden de entrada): los procesos se ejecutan en el orden en el que se lanzan
- SRF (algoritmo por orden de prioridad):  los procesos se ejecutan en el orden de prioridad a excepción del aquel cuya llegada es 0
- SRTF (algoritmo por orden de entrada dependiente del tiempo de ejecución): los procesos se ejecutan en el orden en el que se lanzan dependiendo del tiempo de ejecución del proceso
- ROUND ROBIN (algoritmo por orden entrada en función de un numero): la ejecución de los procesos se realizara por orden de entrada y en función del numero Quantum (tiempo de ejecución que se le otorga a un proceso). Si el tiempo de ejecución es inferior a dicho numero el procesó se ejecutara completamente
- EJEMPLO: si el quantum es 4, el primer proceso dura un tiempo de ejecución de 5 segundos y  el segundo proceso dura un tiempo de ejecución de 6 segundos y el tercer proceso dura un tiempo de ejecución de 3 segundos primero se ejecutara el primer proceso durante 4 segundos después este se pondrá en espera y se ejecutara durante 4 segundos después se ejecutara el tercer proceso hasta que finalice después volverá a iniciarse el primer proceso durante 1 segundo y por ultimo se ejecutara el proceso durante 2 segundos

\\ACTIVIDAD//
realizar un programa en python que reciba una serie de datos de un fichero llamado "procesos.txt" con en 4 grupos de 5 procesos
cada grupo correspondera a cada uno de los algoritmos se debe sacar el promedio del tiempo de espera y el promedio del tiempo de ejecucion de cada grupo