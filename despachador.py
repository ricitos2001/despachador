# -*- coding: utf-8 -*-
import os
import sys
import ast
import importlib

def borrar_consola():
    '''
    limpia el terminal
    '''
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def pausar_programa():
    '''
    pausa el programa mostrando el siguiente mensaje: Pulse una tecla para continuar
    '''
    os.system("pause")

def checkear_version_de_python():
    '''
    comprueba si la version de python es compatible con el programa
    '''
    version_requerida = [(3, 10), (3, 11), (3, 12)]
    version_instalada = sys.version_info[:2]
    if version_instalada in version_requerida:
        verificacion = "version de python: " + str(version_instalada) + "\nla version de python instalada es compatible."
        print(verificacion)
    else:
        verificacion = "la version de python instalada es compatible\nes necesario tener instalado Python3.10, 3.11, o 3.12"
        print(verificacion)

def obtener_librerias_usadas(codigo):
    '''
    obtiene un listado con todas las librerias instaladas
    '''
    tree = ast.parse(codigo)
    librerias = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                librerias.add(alias.name)
        elif isinstance(node, ast.ImportFrom):
            librerias.add(node.module)
    return librerias

def verificar_librerias_programa():
    '''
    comprueba si las librerias necesarias estan istaladas
    '''
    codigo = ""
    librerias_necesarias = obtener_librerias_usadas(codigo)
    librerias_instaladas = all(verificar_libreria(lib) for lib in librerias_necesarias)
    if librerias_instaladas:
        print("Todas las librerías necesarias están instaladas. El programa puede ejecutarse.")
    else:
        print("Error: Al menos una de las librerías necesarias no está instalada. Por favor, instale las librerías faltantes.")

def verificar_libreria(nombre_libreria):
    '''
    comprueba que librerias de python no estan instaladas y que librerias no estan instaladas
    '''
    try:
        importlib.import_module(nombre_libreria)
        libreria_instalada = "la libreria " + str(nombre_libreria) + " esta intalada"
        print(libreria_instalada)
        return True
    except ImportError:
        libreria_sin_instalar = "error: la libreria " + str(nombre_libreria) + " no esta intalada"
        print(libreria_sin_instalar)
        return False

def verificar_archivos(archivo_de_entrada, archivo_de_salida):
    '''
    comprueba si los archivos existen y si su formato es valido o no
    '''
    # en caso de introducir el nombre sin la extension agrega la extension .txt al nombre del archivo antes de realizar la busqueda
    if not (archivo_de_entrada or archivo_de_salida).endswith('.txt'):
        archivo_de_entrada += '.txt'
    # verifica archivo de entrada existe
    if os.path.exists(archivo_de_entrada):
        mensaje = "el archivo " + str(archivo_de_entrada) + " ya existe"
        print(mensaje)
        # Comprobar si la extensión es .txt
        if archivo_de_entrada.lower().endswith('.txt'):
            verificar_extension = "la extensión del archivo es valida"
            print(verificar_extension)
        else:
            mensaje_error = "La extensión del archivo no es valida'.txt'\nse creara un archivo '.txt' con dicho nombre"
            # si el archivo no es .txt crea un archivo nuevo con la extension .txt
            print(mensaje_error)
            with open(archivo_de_entrada + 'txt', 'w') as archivo:
                archivo_creado = "se ha creado el archivo " + str(archivo_de_entrada) + ".txt"
                print(archivo_creado)
    else:
        # si el archivo no existe crea un archivo nuevo con la extension .txt
        mensaje_error = "el archivo " + str(archivo_de_entrada) + " no existe\nse creara un archivo '.txt' con dicho nombre"
        print(mensaje_error)
        with open(archivo_de_entrada + '.txt', 'w') as archivo:
            archivo_creado = "se ha creado el archivo " + str(archivo_de_entrada) + ".txt"
            print(archivo_creado)
    # pausa el programa
    pausar_programa()
    # borra el terminal
    borrar_consola()
    # verifica si el archivo de salida existe
    if os.path.exists(archivo_de_salida):
        mensaje = "el archivo " + str(archivo_de_salida) + " ya existe"
        print(mensaje)
        # comprueba si la extensión es .txt
        if archivo_de_salida.lower().endswith('.txt'):
            verificar_extension = "la extensión del archivo es valida"
            print(verificar_extension)
        else:
            mensaje_error = "La extensión del archivo no es valida'.txt'\nse creara un archivo '.txt' con dicho nombre"
            # si la extension no es .txt crea un archivo nuevo con la extension .txt
            print(mensaje_error)
            with open(archivo_de_salida + '.txt', 'w') as archivo:
                archivo_creado = "se ha creado el archivo " + str(archivo_de_salida) + ".txt"
                print(archivo_creado)
    else:
        # si el archivo no existe crea un archivo nuevo con la extension .txt
        mensaje_error = "el archivo " + str(archivo_de_salida) + " no existe\nse creara un archivo '.txt' con dicho nombre"
        print(mensaje_error)
        with open(archivo_de_salida + '.txt', 'w') as archivo:
            archivo_creado = "se ha creado el archivo " + str(archivo_de_salida) + ".txt"
            print(archivo_creado)

def algoritmo_FCFS(archivo_de_entrada):
    '''
    realiza el algoritmo FCFS para el GRUPO 1
    '''
    procesos_FCFS = []
    # lectura del archivo de entrada
    with open(archivo_de_entrada, 'r') as archivo:
        # saltar la primera linea
        for _ in range(1):
            archivo.readline()
        # leer todas las lineas que esten desde la linea 2 hasta la linea 6
        for _ in range(5):
            linea = archivo.readline().strip()
            partes = linea.split(':')
            procesos_FCFS.append((str(partes[0]), int(partes[1]), int(partes[2])))  
    # marcar el tiempo de retorno inicial para que el bucle funcione correctamente
    tiempo_de_retorno = procesos_FCFS[0][1]
    total_del_tiempo_de_espera = 0
    total_del_tiempo_de_retorno = 0
    # leer el numero de procesos
    numero_de_procesos = len(procesos_FCFS) 
    # ordenar los procesos por su llegada
    procesos_FCFS = sorted(procesos_FCFS, key=lambda x: x[1])  
    for i in range(0, numero_de_procesos):
        # calcular el tiempo de espera
        tiempo_de_llegada = procesos_FCFS[i][1]
        tiempo_de_respuesta = tiempo_de_retorno - tiempo_de_llegada
        tiempo_de_espera = float(tiempo_de_llegada + tiempo_de_respuesta)
        # calcular el tiempo de retorno
        tiempo_de_ejecucion = procesos_FCFS[i][2]
        tiempo_de_retorno = float(tiempo_de_espera + tiempo_de_ejecucion)
        # obtener el promedio del tiempo de espera y del tiempo de retorno
        total_del_tiempo_de_espera += tiempo_de_espera
        total_del_tiempo_de_retorno += tiempo_de_retorno
    promedio_del_tiempo_de_espera = total_del_tiempo_de_espera / numero_de_procesos
    promedio_del_tiempo_de_retorno = total_del_tiempo_de_retorno / numero_de_procesos
    # crear un mensaje que muestre el promedio del tiempo de espera y del tiempo de retorno
    resultados_FCFS = "GRUPO 1 (ALGORITMO FCFS)\npromedio del tiempo de espera: " + str(promedio_del_tiempo_de_espera) + "\npromedio del tiempo de retorno: " + str(promedio_del_tiempo_de_retorno)
    return resultados_FCFS

def algoritmo_SJF(archivo_de_entrada):
    '''
    realiza el algoritmo SJF para el GRUPO 2
    '''
    procesos_SJF = []
    # lectura del archivo de entrada
    with open(archivo_de_entrada, 'r') as archivo:
        # salta la septima linea
        for _ in range(7):
            archivo.readline()
        # lee todas las lineas que esten desde la linea 8 hasta la linea 12
        for _ in range(5):
            linea = archivo.readline().strip()
            partes = linea.split(':')
            procesos_SJF.append((str(partes[0]), int(partes[1]), int(partes[2])))  
    # marca el tiempo de retorno inicial para que el bucle funcione correctamente
    tiempo_de_retorno = 0
    total_del_tiempo_de_espera = 0
    total_del_tiempo_de_retorno = 0
    # lee el numero de procesos
    numero_de_procesos = len(procesos_SJF) 
    # ordena los procesos por el tiempo de ejecucion a excepcion de aquel cuya llegada es 0
    procesos_SJF = sorted(procesos_SJF, key=lambda x: (x[2], x[1]))
    for i in range(0, numero_de_procesos):
        # calcula el tiempo de espera
        tiempo_de_llegada = procesos_SJF[i][1]
        tiempo_de_respuesta = tiempo_de_retorno - tiempo_de_llegada
        tiempo_de_espera = float(tiempo_de_llegada + tiempo_de_respuesta)
        # calcula el tiempo de retorno
        tiempo_de_ejecucion = procesos_SJF[i][2]
        tiempo_de_retorno = float(tiempo_de_espera + tiempo_de_ejecucion)
        # obtiene el promedio del tiempo de espera y del tiempo de retorno
        total_del_tiempo_de_espera += tiempo_de_espera
        total_del_tiempo_de_retorno += tiempo_de_retorno
    promedio_del_tiempo_de_espera = total_del_tiempo_de_espera / numero_de_procesos
    promedio_del_tiempo_de_retorno = total_del_tiempo_de_retorno / numero_de_procesos
    # crea un mensaje que muestre el promedio del tiempo de espera y del tiempo de retorno
    resultados_SJF = "GRUPO 2 (ALGORITMO SJF)\npromedio del tiempo de espera: " + str(promedio_del_tiempo_de_espera) + "\npromedio del tiempo de retorno: " + str(promedio_del_tiempo_de_retorno)
    return resultados_SJF

#!\\ HACER EL ALGORITMO SRTF //!#
def algoritmo_SRTF(archivo_de_entrada):
    '''
    realiza el algoritmo SRTF para el GRUPO 3
    '''
    procesos_SRTF = []
    # lectura del archivo de entrada
    with open(archivo_de_entrada, 'r') as archivo:
        # salta la decimo tercera linea
        for _ in range(13):
            archivo.readline()
        # lee todas las lineas que esten desde la linea 14 hasta la linea 18
        for _ in range(5):
            linea = archivo.readline().strip()
            partes = linea.split(':')
            procesos_SRTF.append((str(partes[0]), int(partes[1]), int(partes[2])))  
    # marca el tiempo de retorno inicial para que el bucle funcione correctamente
    tiempo_de_retorno = 0
    total_del_tiempo_de_espera = 0
    total_del_tiempo_de_retorno = 0
    # lee el numero de procesos
    numero_de_procesos = len(procesos_SRTF)

    promedio_del_tiempo_de_espera = total_del_tiempo_de_espera / numero_de_procesos
    promedio_del_tiempo_de_retorno = total_del_tiempo_de_retorno / numero_de_procesos
    # crea un mensaje que muestre el promedio del tiempo de espera y del tiempo de retorno
    resultados_SRTF = "GRUPO 3 (ALGORITMO SRTF)\npromedio del tiempo de espera: " + str(promedio_del_tiempo_de_espera) + "\npromedio del tiempo de retorno: " + str(promedio_del_tiempo_de_retorno)
    return resultados_SRTF
#!\\ HACER EL ALGORITMO ROUND ROBIN //!#
def algoritmo_ROUND_ROBIN(archivo_de_entrada):
    '''
    realiza el algoritmo SRTF para el GRUPO 3
    '''
    procesos_ROUND_ROBIN = []
    # lectura del archivo de entrada
    with open(archivo_de_entrada, 'r') as archivo:
        # salta la decimo novena linea
        for _ in range(13):
            archivo.readline()
        # lee todas las lineas que esten desde la linea 20 hasta la linea 24
        for _ in range(5):
            linea = archivo.readline().strip()
            partes = linea.split(':')
            procesos_ROUND_ROBIN.append((str(partes[0]), int(partes[1]), int(partes[2])))  
    # define el valor quantico (quantum)
    quantum = 3
    # marca el tiempo de retorno inicial para que el bucle funcione correctamente
    tiempo_de_retorno = 0
    total_del_tiempo_de_espera = 0
    total_del_tiempo_de_retorno = 0
    # lee el numero de procesos
    numero_de_procesos = len(procesos_ROUND_ROBIN)
    
    for i in range(0, numero_de_procesos):
        # calcular el tiempo de espera
        tiempo_de_llegada = procesos_ROUND_ROBIN[i][1]
        tiempo_de_respuesta = tiempo_de_retorno - tiempo_de_llegada
        tiempo_de_espera = float(tiempo_de_llegada + tiempo_de_respuesta)
        # calcular el tiempo de retorno
        tiempo_de_ejecucion = procesos_ROUND_ROBIN[i][2]
        tiempo_de_retorno = float(tiempo_de_espera + tiempo_de_ejecucion)
        # obtener el promedio del tiempo de espera y del tiempo de retorno
        total_del_tiempo_de_espera += tiempo_de_espera
        total_del_tiempo_de_retorno += tiempo_de_retorno
    
    promedio_del_tiempo_de_espera = total_del_tiempo_de_espera / numero_de_procesos
    promedio_del_tiempo_de_retorno = total_del_tiempo_de_retorno / numero_de_procesos
    # crea un mensaje que muestre el promedio del tiempo de espera y del tiempo de retorno
    resultados_ROUND_ROBIN = "GRUPO 4 (ALGORITMO ROUND ROBIN)\npromedio del tiempo de espera: " + str(promedio_del_tiempo_de_espera) + "\npromedio del tiempo de retorno: " + str(promedio_del_tiempo_de_retorno)
    return resultados_ROUND_ROBIN

def escribir_resultados(resultados_FCFS, resultados_SJF, archivo_de_salida):
    '''
    escribe los resultados en el archivo de salida
    '''
    with open(archivo_de_salida, 'w', encoding='utf8') as archivo:
        archivo.write(resultados_FCFS + '\n')
        archivo.write(resultados_SJF + '\n')
        # archivo.write(resultados_SRTF + '\n')
        # archivo.write(resultados_ROUND_ROBIN + '\n')

def main():
    # borra el terminal
    borrar_consola()
    # comprueba si la version de python es compatible con el programa
    checkear_version_de_python()
    # comprueba si las librerias necesarias estan istaladas
    verificar_librerias_programa()
    # pausa el programa
    pausar_programa()
    # borra el terminal
    borrar_consola()
    print("---------GESTOR DE PROCESOS---------")
    # pausa el programa
    pausar_programa()
    # borra el terminal
    borrar_consola()
    # selecciona el archivo de entrada
    archivo_de_entrada = "procesos.txt"
    # selecciona el archivo de salida
    archivo_de_salida = "salida.txt"
    # verifica si existen los archivos y si su extension es valida
    verificar_archivos(archivo_de_entrada, archivo_de_salida)
    pausar_programa()
    # borra el terminal
    borrar_consola()
    # selecciona el archivo de entrada
    resultados_FCFS = algoritmo_FCFS(archivo_de_entrada)
    resultados_SJF = algoritmo_SJF(archivo_de_entrada)
    #resultados_SRTF = algoritmo_SRTF(archivo_de_entrada)
    #resultados_ROUND_ROBIN = algoritmo_ROUND_ROBIN(archivo_de_entrada)
    escribir_resultados(resultados_FCFS, resultados_SJF, archivo_de_salida)
    print(resultados_FCFS)
    print(resultados_SJF)
    #print(resultados_SRTF)
    #print(resultados_ROUND_ROBIN)
    mensaje_de_importacion = "\nlos resultados han sido importados con exito"
    # muestra los resultados y emite un mensaje que indica que los resultados fueron importados en el archivo de salida
    print(mensaje_de_importacion)
    # pausa el programa
    pausar_programa()
    # borra el terminal
    borrar_consola()

if __name__ == "__main__":
    main()

# verificar si el archivo de entrada y el de salida tienen contenido
# si el archivo de entrada no tiene contenido mostrar un mensaje indicando que introduzca el contenido
# si el archivo de salida tiene contenido sobreescribir dicho contenido
# verificar si el contenido del archivo de entrada (datos introducidos) son correctos (estan escritos de forma correcta)
# hacer el SRTF y el ROUND ROBIN