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
    if os.name == "posix":
        os.system(input("presiona intro para continuar..."))
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
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

def buscar_archivo(nombre_del_archivo):
    '''
    busca un archivo que coincida con el nombre del archivo sin la extension
    '''
    try:
        # lista todos los archivos en el directorio actual
        archivos = os.listdir('.')
        for archivo in archivos:
            # divide los archivos por su nombre y su formato
            partes_del_archivo_encontrado = os.path.splitext(archivo) 
            nombre_archivo_encontrado = partes_del_archivo_encontrado[0]
            if nombre_archivo_encontrado == nombre_del_archivo:
                return archivo
    except FileNotFoundError:
        # si el archivo no ha sido encontrado muestra un mensaje de error
        raise FileNotFoundError("El archivo " + nombre_del_archivo + " no existe")

def verificar_formato(archivo_encontrado, extension_del_archivo):
    '''
    verifica si el formato del archivo encontrado es el adecuado
    '''
    # verifica si la extensión del archivo es correcta
    if archivo_encontrado.endswith(extension_del_archivo):
        print("El archivo " + archivo_encontrado + " existe y su formato es valido.")
    else:
        # si la extension del archivo no es valido muestra un mensaje de error
        raise ValueError("El formato del archivo " + archivo_encontrado + " no es valido.")

def verificar_contenido_de_entrada(archivo_de_entrada):
    '''
    verifica si el archivo de entrada tiene contenido
    '''
    with open(archivo_de_entrada, 'r') as file:
        contenido = file.read().strip()
        if contenido:
            print("El archivo tiene contenido.")
        else:
            # lanzar un mensaje de error en caso de que no lo tenga
            raise ValueError("El archivo está vacío.")

def verificar_entrada(archivo_de_entrada):
    partes_del_archivo = archivo_de_entrada.split('.')
    nombre_del_archivo = partes_del_archivo[0]
    extension_del_archivo = '.' + partes_del_archivo[1]
    archivo_encontrado = buscar_archivo(nombre_del_archivo)
    verificar_formato(archivo_encontrado, extension_del_archivo)

def verificar_salida(archivo_de_salida):
    partes_del_archivo = archivo_de_salida.split('.')
    nombre_del_archivo = partes_del_archivo[0]
    extension_del_archivo = '.' + partes_del_archivo[1]
    archivo_encontrado = buscar_archivo(nombre_del_archivo)
    verificar_formato(archivo_encontrado, extension_del_archivo)

def algoritmo_FCFS(archivo_de_entrada):
    '''
    realiza el algoritmo FCFS para el GRUPO 1
    '''
    procesos_FCFS = []
    with open(archivo_de_entrada, 'r') as archivo:
        # saltar la primera proceso
        for _ in range(1):
            archivo.readline()
        # leer todas las lineas que esten desde la proceso 2 hasta la proceso 6
        for _ in range(5):
            proceso = archivo.readline().strip()
            partes_del_proceso = proceso.split(':')
            if len(partes_del_proceso) == 3 and partes_del_proceso[0].startswith('P') and partes_del_proceso[0][1:].isdigit() and partes_del_proceso[1].isdigit() and partes_del_proceso[2].isdigit():
                procesos_FCFS.append((str(partes_del_proceso[0]), int(partes_del_proceso[1]), int(partes_del_proceso[2])))
            else:
                raise ValueError("Error de formato en el archivo de " + str(archivo_de_entrada) + ": " + str(proceso.strip()))
    # marca el tiempo de retorno inicial para que el bucle funcione correctamente
    tiempo_de_retorno = procesos_FCFS[0][1]
    total_del_tiempo_de_espera = 0
    total_del_tiempo_de_retorno = 0
    # lee el numero de procesos
    numero_de_procesos = len(procesos_FCFS) 
    # ordena los procesos por su llegada
    procesos_FCFS = sorted(procesos_FCFS, key=lambda x: x[1])  
    for i in range(0, numero_de_procesos):
        # calcula el tiempo de espera
        tiempo_de_llegada = procesos_FCFS[i][1]
        tiempo_de_respuesta = tiempo_de_retorno - tiempo_de_llegada
        tiempo_de_espera = float(tiempo_de_llegada + tiempo_de_respuesta)
        # calcula el tiempo de retorno
        tiempo_de_respuesta = procesos_FCFS[i][2]
        tiempo_de_retorno = float(tiempo_de_espera + tiempo_de_respuesta)
        # obtiene el promedio del tiempo de espera y del tiempo de retorno
        total_del_tiempo_de_espera += tiempo_de_espera
        total_del_tiempo_de_retorno += tiempo_de_retorno
    promedio_del_tiempo_de_espera = total_del_tiempo_de_espera / numero_de_procesos
    promedio_del_tiempo_de_retorno = total_del_tiempo_de_retorno / numero_de_procesos
    # crea un mensaje que muestre el promedio del tiempo de espera y del tiempo de retorno
    resultados_FCFS = "GRUPO 1 (ALGORITMO FCFS)\npromedio del tiempo de espera: " + str(promedio_del_tiempo_de_espera) + " segundos\npromedio del tiempo de retorno: " + str(promedio_del_tiempo_de_retorno) + " segundos"
    return resultados_FCFS

def algoritmo_SJF(archivo_de_entrada):
    '''
    realiza el algoritmo SJF para el GRUPO 2
    '''
    procesos_SJF = []
    with open(archivo_de_entrada, 'r') as archivo:
        # salta la septima proceso
        for _ in range(7):
            archivo.readline()
        # lee todas las lineas que esten desde la proceso 8 hasta la proceso 12
        for _ in range(5):
            proceso = archivo.readline().strip()
            partes_del_proceso = proceso.split(':')
            if len(partes_del_proceso) == 3 and partes_del_proceso[0].startswith('P') and partes_del_proceso[0][1:].isdigit() and partes_del_proceso[1].isdigit() and partes_del_proceso[2].isdigit():
                procesos_SJF.append((str(partes_del_proceso[0]), int(partes_del_proceso[1]), int(partes_del_proceso[2])))
            else:
                raise ValueError("Error de formato en el archivo de " + str(archivo_de_entrada) + ": " + str(proceso.strip()))
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
        tiempo_de_respuesta = procesos_SJF[i][2]
        tiempo_de_retorno = float(tiempo_de_espera + tiempo_de_respuesta)
        # obtiene el promedio del tiempo de espera y del tiempo de retorno
        total_del_tiempo_de_espera += tiempo_de_espera
        total_del_tiempo_de_retorno += tiempo_de_retorno
    promedio_del_tiempo_de_espera = total_del_tiempo_de_espera / numero_de_procesos
    promedio_del_tiempo_de_retorno = total_del_tiempo_de_retorno / numero_de_procesos
    # crea un mensaje que muestre el promedio del tiempo de espera y del tiempo de retorno
    resultados_SJF = "GRUPO 2 (ALGORITMO SJF)\npromedio del tiempo de espera: " + str(promedio_del_tiempo_de_espera) + " segundos\npromedio del tiempo de retorno: " + str(promedio_del_tiempo_de_retorno) + " segundos"
    return resultados_SJF

def algoritmo_SRTF(archivo_de_entrada):
    '''
    realiza el algoritmo SRTF para el GRUPO 3
    '''
    procesos_SRTF = []
    with open(archivo_de_entrada, 'r') as archivo:
        # salta la decimo tercera proceso
        for _ in range(13):
            archivo.readline()
        # lee todas las lineas que esten desde la proceso 14 hasta la proceso 18
        for _ in range(5):
            proceso = archivo.readline().strip()
            partes_del_proceso = proceso.split(':')
            if len(partes_del_proceso) == 3 and partes_del_proceso[0].startswith('P') and partes_del_proceso[0][1:].isdigit() and partes_del_proceso[1].isdigit() and partes_del_proceso[2].isdigit():
                procesos_SRTF.append((str(partes_del_proceso[0]), int(partes_del_proceso[1]), int(partes_del_proceso[2])))
            else:
                raise ValueError("Error de formato en el archivo de " + str(archivo_de_entrada) + ": " + str(proceso.strip()))
    # marca el tiempo de retorno inicial para que el bucle funcione correctamente
    tiempo_de_respuesta = 0
    total_del_tiempo_de_espera = 0
    total_del_tiempo_de_retorno = 0
    procesos_en_ejecucion = []
    # lee el numero de procesos
    numero_de_procesos = len(procesos_SRTF)
    while procesos_SRTF or procesos_en_ejecucion:
        # agrega los procesos que han llegado al tiempo actual
        while procesos_SRTF and procesos_SRTF[0][1] <= tiempo_de_respuesta:
            procesos_en_ejecucion.append(procesos_SRTF.pop(0))
            procesos_en_ejecucion.sort(key=lambda x: x[2])  # Ordenar por el tiempo restante más corto
        if procesos_en_ejecucion:
            tiempo_de_llegada = procesos_en_ejecucion.pop(0)
            # calcula el tiempo de espera
            tiempo_espera = tiempo_de_respuesta - tiempo_de_llegada[1]
            tiempo_de_respuesta += tiempo_de_llegada[2]
            # calcula el tiempo de retorno
            tiempo_retorno = tiempo_de_respuesta - tiempo_de_llegada[1]
            total_del_tiempo_de_espera += tiempo_espera
            total_del_tiempo_de_retorno += tiempo_retorno
    # ordenar los procesos por su llegada y por su tiempo de ejecucion
    procesos_SRTF = sorted(procesos_SRTF, key=lambda x: x[1])
    promedio_del_tiempo_de_espera = total_del_tiempo_de_espera / numero_de_procesos
    promedio_del_tiempo_de_retorno = total_del_tiempo_de_retorno / numero_de_procesos
    # crea un mensaje que muestre el promedio del tiempo de espera y del tiempo de retorno
    resultados_SRTF = "GRUPO 3 (ALGORITMO SRTF)\npromedio del tiempo de espera: " + str(promedio_del_tiempo_de_espera) + " segundos\npromedio del tiempo de retorno: " + str(promedio_del_tiempo_de_retorno) + " segundos"
    return resultados_SRTF

def algoritmo_ROUND_ROBIN(archivo_de_entrada):
    '''
    realiza el algoritmo ROUND ROBIN para el GRUPO 4
    '''
    procesos_ROUND_ROBIN = []
    # lista que define una cola de procesos en ejecucion
    cola_de_procesos = []
    # lista que define el valor quantico (quantum)
    quantum = []
    with open(archivo_de_entrada, 'r') as archivo:
        # salta la decimo novena proceso
        for _ in range(19):
            archivo.readline()
        # lee la linea 20 
        for _ in range(1):
            # obtiene los datos del valor cuantico o quantum
            linea_del_valor_cuantico = archivo.readline().strip()
            # separa y lista los valores de la linea
            valor_cuantico = linea_del_valor_cuantico.split(' = ')
            # obtiene el valor cuantico o cuantum y lo introduce en la lista quantum
            quantum.append(int(valor_cuantico[1]))
        # lee todas las lineas que esten desde la proceso 21 hasta la proceso 25
        for _ in range(5):
            proceso = archivo.readline().strip()
            partes_del_proceso = proceso.split(':')
            #*se remplaza la tupla por una lista para añadir una unidad de tiempo restante en la cuarta posicion
            if len(partes_del_proceso) == 3 and partes_del_proceso[0].startswith('P') and partes_del_proceso[0][1:].isdigit() and partes_del_proceso[1].isdigit() and partes_del_proceso[2].isdigit():
                procesos_ROUND_ROBIN.append([str(partes_del_proceso[0]), int(partes_del_proceso[1]), int(partes_del_proceso[2]), 0])
            else:
                raise ValueError("error de formato en el archivo de " + str(archivo_de_entrada) + ": " + str(proceso.strip()))
    # marca el tiempo de retorno inicial para que el bucle funcione correctamente
    tiempo_de_respuesta = 0
    total_del_tiempo_de_espera = 0
    total_del_tiempo_de_retorno = 0
    # lee el numero de procesos
    numero_de_procesos = len(procesos_ROUND_ROBIN)
    while procesos_ROUND_ROBIN or cola_de_procesos:
        # agregaa procesos que han llegado al tiempo actual a la cola de procesos
        while procesos_ROUND_ROBIN and procesos_ROUND_ROBIN[0][1] <= tiempo_de_respuesta:
            cola_de_procesos.append(procesos_ROUND_ROBIN.pop(0))
        if cola_de_procesos:
            tiempo_de_llegada = cola_de_procesos.pop(0)
            # calcular el tiempo de espera
            tiempo_espera = tiempo_de_respuesta - tiempo_de_llegada[1] - tiempo_de_llegada[3]
            tiempo_ejecucion = min(quantum[0], tiempo_de_llegada[2])
            tiempo_de_respuesta += tiempo_ejecucion
            tiempo_de_llegada[2] -= tiempo_ejecucion
            tiempo_de_llegada[3] += tiempo_ejecucion
            if tiempo_de_llegada[2] > 0:
                # si el proceso aún no ha terminado se vuelve a añadir a la cola
                cola_de_procesos.append(tiempo_de_llegada)
            else:
                # calcular del tiempo de retorno
                tiempo_de_retorno = tiempo_de_respuesta - tiempo_de_llegada[1]
                # obtener el promedio del tiempo de espera y del tiempo de retorno
                total_del_tiempo_de_espera += tiempo_espera
                total_del_tiempo_de_retorno += tiempo_de_retorno
        else:
            tiempo_de_respuesta += 1  # incrementa el tiempo si no hay procesos listos
    promedio_del_tiempo_de_espera = total_del_tiempo_de_espera / numero_de_procesos
    promedio_del_tiempo_de_retorno = total_del_tiempo_de_retorno / numero_de_procesos
    # crea un mensaje que muestre el promedio del tiempo de espera y del tiempo de retorno
    resultados_ROUND_ROBIN = "GRUPO 4 (ALGORITMO ROUND ROBIN)\npromedio del tiempo de espera: " + str(promedio_del_tiempo_de_espera) + " segundos\npromedio del tiempo de retorno: " + str(promedio_del_tiempo_de_retorno) + " segundos"
    return resultados_ROUND_ROBIN

def verificar_contenido_de_salida(archivo_de_salida):
    '''
    verifica si el archivo de salida tiene contenido o no
    '''
    # verifica si el archivo ya tiene resultados escritos
    with open(archivo_de_salida, 'r') as file:
        resultados_existentes = file.read().strip()
    # escribe los resultados acorde a los procesos del archivo de entrada
    if resultados_existentes:
        # emite un mensaje diciendo que los datos han sido actualizados
        mensaje_de_importacion = "\nlos resultados han sido actualizados con exito"
    else:
        mensaje_de_importacion = "\nlos resultados han sido importados con exito"
    return mensaje_de_importacion

def escribir_resultados(resultados_FCFS, resultados_SJF, resultados_SRTF, resultados_ROUND_ROBIN, archivo_de_salida):
    '''
    escribe los resultados en el archivo de salida
    '''
    # verifica si el archivo ya tiene resultados escritos
    with open(archivo_de_salida, 'r') as file:
        resultados_existentes = file.read().strip()
    # escribe los resultados acorde a los procesos del archivo de entrada
    if resultados_existentes:
        # emite un mensaje diciendo que los datos han sido actualizados
        print("los datos han sido actualizados con exito")
    with open(archivo_de_salida, 'w', encoding='utf8') as archivo:
        archivo.write(resultados_FCFS + '\n')
        archivo.write(resultados_SJF + '\n')
        archivo.write(resultados_SRTF + '\n')
        archivo.write(resultados_ROUND_ROBIN + '\n')

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
    try:
        # selecciona el archivo de entrada
        archivo_de_entrada = "procesos.txt"
        # selecciona el archivo de salida
        archivo_de_salida = "salida.txt"
        # verifica si existen el archivo de entrada y si su extension es valida
        verificar_entrada(archivo_de_entrada)
        # pausa el programa
        pausar_programa()
        # verifica si existen el archivo de salida y si su extension es valida
        verificar_salida(archivo_de_salida)
        # pausa el programa
        pausar_programa()
        # borra el terminal
        borrar_consola()
        # genera los resultados de cada proceso
        resultados_FCFS = algoritmo_FCFS(archivo_de_entrada)
        resultados_SJF = algoritmo_SJF(archivo_de_entrada)
        resultados_SRTF = algoritmo_SRTF(archivo_de_entrada)
        resultados_ROUND_ROBIN = algoritmo_ROUND_ROBIN(archivo_de_entrada)
        # importa los resultados en el archivo de salida
        escribir_resultados(resultados_FCFS, resultados_SJF, resultados_SRTF, resultados_ROUND_ROBIN, archivo_de_salida)
        # muestra los resultados por consola y emite un mensaje indicando que los resultados fueron importados en el archivo de salida
        print(resultados_FCFS)
        print(resultados_SJF)
        print(resultados_SRTF)
        print(resultados_ROUND_ROBIN)
        mensaje_de_importacion = verificar_contenido_de_salida(archivo_de_salida)
        print(mensaje_de_importacion)
        # pausa el programa
        pausar_programa()
        # borra el terminal
        borrar_consola()
    except (FileNotFoundError, ValueError) as error:
        print(error)
        # pausa el programa
        pausar_programa()
        # borra el terminal
        borrar_consola()

if __name__ == "__main__":
    main()