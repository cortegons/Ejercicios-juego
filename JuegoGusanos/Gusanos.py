import random
import time

def crearGusanos(gusanos):
    print("--Creando los gusanos en las ubicaciones--")
    # abrir el archivo con los datos
    archivo = open("gusanos.txt")
    # leer archivo
    contenido = archivo.read()
    # separar por comas
    lista = contenido.split(",")
    # asignar valores a la lista de gusanos
    gusanos[0] = int(lista[0])
    gusanos[1] = int(lista[1])
    gusanos[2] = int(lista[2])
    gusanos[3] = int(lista[3])
    
    time.sleep(2)

def mostrar(gusanos):
    # se muestran los gusanos con el formato deseado
    print("----------------")
    print("FB:", gusanos[0], "|", "AR:", gusanos[1])
    print("----------------")
    print("NA:", gusanos[2], "|", "PP:", gusanos[3])
    print("----------------")
    time.sleep(2)

def disparar(gusanos):
    # Se reducen 10 gusanos en la ubicación elegida.
    posicionADisparar = int(input("--Ingrese la ubicación a disparar (0, 1, 2 ó 3)--"))
    
    if (posicionADisparar == 0):
        print("--Un enorme disparo se dirige a Fondo de Bikini--")
    elif(posicionADisparar == 1):
        print("--Un enorme disparo se dirige a Arraki--")
    elif(posicionADisparar == 2):
        print("--Un enorme disparo se dirige a Namekusei--")
    elif(posicionADisparar == 3):
        print("--Un enorme disparo se dirige a Pueblo Paleta--")
    
    
    if (gusanos[posicionADisparar] - 10 <= 0):
        gusanos[posicionADisparar] = 0
    else:
        gusanos[posicionADisparar] = gusanos[posicionADisparar]-10
    time.sleep(2)

def lanzaPesticida(gusanos):
    # La cantidad de gusanos en todas las zonas se divide a la mitad. 
    print("--Se rocía pesticida en todas las ubicaciones--")
    gusanos[1] = gusanos[1] - gusanos[1]//2
    gusanos[0] = gusanos[0] - gusanos[0]//2
    gusanos[2] = gusanos[2] - gusanos[2]//2
    gusanos[3] = gusanos[3] - gusanos[3]//2
    time.sleep(2)
    
def vientoGuadalupe(gusanos):
    numAleatorio = random.randint(0,3)
    if (numAleatorio == 0):
        print("--Un viento milagroso pasa por Fondo de Bikini--")
    elif(numAleatorio == 1):
        print("--Un viento milagroso pasa por Arraki--")
    elif(numAleatorio == 2):
        print("--Un viento milagroso pasa por Namekusei--")
    elif(numAleatorio == 3):
        print("--Un viento milagroso pasa por Pueblo Paleta--")
    gusanos[numAleatorio] = gusanos[numAleatorio] + 10
    time.sleep(2)

def lluviaAcida(gusanos):
    # los gusanos en la ubicación elegida, se reducen a 0
    posicionADisparar = int(input("--Ingrese la ubicación a disparar (0, 1, 2 ó 3)--"))
    if (posicionADisparar == 0):
        print("--Una nube de lluvia ácida se dirige a Fondo de Bikini--")
    elif(posicionADisparar == 1):
        print("--Una nube de lluvia ácida se dirige a Arraki--")
    elif(posicionADisparar == 2):
        print("--Una nube de lluvia ácida se dirige a Namekusei--")
    elif(posicionADisparar == 3):
        print("--Una nube de lluvia ácida se dirige a Pueblo Paleta--")   
    gusanos[posicionADisparar] = 0
    time.sleep(2)

def fraseTia():
    #frase aleatoria de la tía
    numAleatorio = random.randint(0,5)
    if(numAleatorio == 0):
        print("Sobri, tanto gusano que ha matado, pero, ¿pa' cuándo la novia?")
    if(numAleatorio == 1):
        print("Sobri, ¿su mamá si le dijo que iba a comprar de la revista del Avon?")
    if(numAleatorio == 2):
        print("Cómo estás de grande, sobri. Me saludas a tu mami.")
    if(numAleatorio == 3):
        print("Tan lindo mi sobrino como acaba con esos gusanos, deles duro.")
    if(numAleatorio == 4):
        print("Sobri, usted que anda tan programador, venga reinicieme el router.")
    if(numAleatorio == 5):
        print("Dios te bendinga sobri, y a esos gusanos también.")
 
def misterio(gusanos):
    print("¡Es hora de bailar")
    print("Sino balias, pierdes ;)")
    horaBaile = int(input("--Ingrese un número"))
    if(horaBaile == 0):
      print("Todos los gusanos que estén en Fondo de Bikini, deben bailar la Macarena")
    elif(horaBaile == 1):
      print("Todos los gusanos que estén en Arraki, deben bailar salsa")
    elif (horaBaile == 2):
      print("Todos los gusanos que estén en Namekusei, deben bailar el Limbo")
    elif horaBaile == 3:
      print("Todos los gusanos que estén en Pueblo Paleta, deben bailar el Chuchuwa")
    time.sleep(2)
    
def promedioGusanos(gusanos):
    # inicia el acumulador
    acumulador = 0
    for x in gusanos:
        acumulador = acumulador + x
    # divide la suma entre la cantidad de zonas
    promedio = acumulador / len(gusanos)
    print("El promedio de gusanos es:", promedio)
    time.sleep(2)
    
gusanos = [0, 0, 0, 0]
# creación de gusanos con entrada por pantalla
crearGusanos(gusanos)
# ciclo infinito hasta derrotar todos los gusanos
while(True):
    mostrar(gusanos)
    # posibles opciones por parte del usuario
    print("--Ingrese--")
    print("1) para disparar a gusanos de una ubicación particular")
    print("2) para lanzar pesticida a todas las ubicaciones")
    print("3) para llamar al viento de la rosa de guadalupe")
    print("4) para desatar la poderosa lluvia ácida concentrada")
    print("5) para obtener sabiduría de la tía")
    print("6) para una acción misteriosa")
    print("7) para calcular el promedio de los gusanos")
    accion = int(input())
    # condicionales con las funciones posibles
    if(accion == 1):
        disparar(gusanos)
    elif(accion == 2):
        lanzaPesticida(gusanos)
    elif(accion == 3):
        vientoGuadalupe(gusanos)
    elif(accion == 4):
        lluviaAcida(gusanos)
    elif(accion == 5):
        fraseTia()
    elif(accion == 6):
        misterio(gusanos)
    elif(accion == 7):
        promedioGusanos(gusanos)
    # condicional para terminar el juego
    if(gusanos[0] == 0 and gusanos[1] == 0 and gusanos[2] == 0 and gusanos[3] == 0):
        mostrar(gusanos)
        print("----------------------------------")
        print("----------------------------------")
        print("Felicitaciones, salvaste la Galaxia")
        print("----------------------------------")
        print("----------------------------------")
        break
