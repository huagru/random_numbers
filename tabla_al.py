# Generador de una tabla de números aleatorios en formato txt, pdf o csv para imprimir.

# ÍNDICE / INDEX:
# 1- Módulos / Modules.
# 2- Estado del script y opciones elegidas/ Script state and selected options.
# 3- Función limpiar la pantalla / function to clear the screen.
# 4- Función para elegir idioma / function for language selection.
# 5- Función para elegir cuántos números se van a generar / Function to specify how many numbers to generate.
# 6- Número inicial / initial number
# 7- Número final / ending number
# 8- Formato del archivo de salida / format of generated file
# 9- Función que genera los números aleatorios / function that generates the random numbers.
# 10- Función que genera el archivo .txt.
# 11- Función que genera el archivo .csv. 







# 1- Módulos importados:
# Módulo para aleatorizar:
import random
import csv   

# Módulo para manejar la consola de windows y linux creando una funcion clear(): 
from os import system, name 




# 2- Opciones y estados / options and states:
opciones = {
    "idioma": 1, #1: español, 2: english
    "cantidad_numeros": 0,
    "valor_inicio": 0,
    "valor_fin": 0,
    "formato_archivo": 0, #0: txt, 1: csv
    
}

numeros_generados = []



# 3- Función para limpiar la pantalla / Function to clear the screen:
def borrar(): 
  
    #para Windows
    if name == 'nt': 
        _ = system('cls') 
  
    #para Linux y Mac 
    else: 
        _ = system('clear')


# 4- Selector de idioma / language selector
def elegir_idioma():
    idioma = int(input("""Elija idioma / Select language: 
                            1) Para español 
                            2) For english
                            """))
    
    opciones["idioma"] = idioma




# 5- Elegir cuantos números generar/ select how many numbers to generate:
def elegir_cantidad_numeros():
    if opciones["idioma"] == 1:
        cantidad = int(input("¿Cuántos números desea generar?: "))

    elif opciones["idioma"] == 2:
        cantidad = int(input("How many numbers you want to generate?: "))  

    opciones["cantidad_numeros"] = cantidad      


# 6 - Elegir número inicial / select starting number:
def inicio():
    if opciones["idioma"] == 1:
        inicio = int(input("¿Cuál es el número de inicio?: "))

    elif opciones["idioma"] == 2:
        inicio = int(input("From which number start?: "))

    opciones["valor_inicio"] = inicio    
        

# 7 - Elegir número final / select ending number:
def final():
    if opciones["idioma"] == 1:
        final = int(input("¿Hasta qué número?: "))

    elif opciones["idioma"] == 2:
        final = int(input("To which number?: "))

    opciones["valor_fin"] = final




# 8 - Elegir formato del archivo de salida:
def formato_archivo():
    if opciones["idioma"] == 1:
        formato = int(input("""Elija el formato del archivo a generar: 
                            1) .txt 
                            2) .csv
                            """))

    elif opciones["idioma"] == 2:
        formato = int(input("""Select the extension of the file to generate: 
                            1) .txt 
                            2) .csv
                            """))   


    opciones["formato_archivo"] = formato




# 9 - Función que genera los números aleatorios / function that generates the random numbers:
def numeros():
    i = 0
    while i < opciones["cantidad_numeros"]:
        numero = random.randint(opciones["valor_inicio"], opciones["valor_fin"])
        numeros_generados.append(numero)

        i += 1

    




# 10 - Generar archivos en .txt / Generating .txt files:
def generar_archivo_txt():
    if opciones["idioma"] == 1:
        nombre_archivo = input("Nombre del archivo .txt a generar?: ")

    elif opciones["idioma"] == 2:
        nombre_archivo = input("Name of the .txt output file?: ")    
        
    archivo = open(nombre_archivo, "a")

    for i in numeros_generados:
        archivo.write(str(i) + " ")
    
    archivo.close()



# 11 - Generar archivos en csv / Generate .csv files:    
def generar_archivo_csv():
    
    if opciones["idioma"] == 1:
        nombre_archivo = input("Nombre del archivo .csv a generar?: ")

    elif opciones["idioma"] == 2:
        nombre_archivo = input("Csv filename to generate?: ")     
    

    with open(nombre_archivo, 'w', newline="") as file:
        writer = csv.writer(file, delimiter="\t", lineterminator="\n")
    
        writer.writerow(numeros_generados)



    

# Inicio
print("CREADOR DE TABLA DE NÚMEROS ALEATORIOS / RANDOM NUMBERS TABLE GENERATOR")

# Elegimos idioma:
elegir_idioma()

borrar()
print("CREADOR DE TABLA DE NÚMEROS ALEATORIOS / RANDOM NUMBERS TABLE GENERATOR")

# Elegimos las opciones:
inicio()
final()  
elegir_cantidad_numeros()
formato_archivo()


# Generamos los números:
numeros()

# Generamos el archivo con la tabla y el formato elegido:
if opciones["formato_archivo"] == 1:
    generar_archivo_txt()

elif opciones["formato_archivo"] == 2:
    generar_archivo_csv()  


# Mensaje de salida:
if opciones["idioma"] == 1:
    print("Tabla generada!")

elif opciones["idioma"] == 2:
    print("Table generated!")