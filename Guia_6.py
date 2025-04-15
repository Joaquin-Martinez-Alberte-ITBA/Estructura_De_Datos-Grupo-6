import csv

#EJercicio 1
diccionario = {'Nicolas':{'Norte':3528, 'Sur':2400, 'Este':1200, 'Oeste':8200}
               , 'Daniela':{'Norte':3824, 'Sur':6786, 'Este':5598, 'Oeste':3612}
               , 'Maria':{'Norte':8008, 'Sur':4653, 'Este':8425, 'Oeste':1000}
               , 'Francisco':{'Norte':5833, 'Sur':6356, 'Este':2548, 'Oeste':1386}}

def modificar_ventas():
    persona = input('Ingrese la persona a modificar: ')
    while persona.capitalize() not in diccionario:
        persona = input('Vuelva a ingresar la persona a modificar: ')
    zona = input('Ingrese zona a modificar: ')
    while zona.capitalize() not in diccionario[persona]:
        zona = input('Vuelva a ingresar la zona: ')
    try:
        valor = int(input('Ingresar un valor nuevo de ventas: '))
        while valor < 0:
         valor = int(input('Ingresar un valor nuevo de ventas: '))
        diccionario[persona][zona] = valor
    except ValueError:
        print('Valor ingresado incorrecto: ')

def ver_ventas_totales():
    cant_ventas = 0
    for  persona in diccionario:
        for zona in diccionario[persona]:
            cant_ventas += diccionario[persona][zona]
    
    return cant_ventas

def zona_mayor_cant_ventas():
    cant_ventas_por_zona = {'Norte':0, 'Sur':0, 'Este':0, 'Oeste':0}
    for persona in diccionario:
        for zona in diccionario[persona]:
            cant_ventas_por_zona[zona] += diccionario[persona][zona]

    



#Ejercicio 2

diccionario= {'a':2,'n':3,'f':5,'z':5}
lista=['cono','mazazo','fanzine','fhan','marsupial']
def puntaje_maximo(lista,diccionario):
    palabra_grande=''
    s

for letra in palabr    0=am
    
    
    return








#Ejercicio 3

lista=[{"Pan":22.8,"Pollo":33.85}, {"Mermelada":42.5, "Pan":23.55,"Tomate":18.3},{"Pan":28.0,"Tomate":19.5,"Pollo":34.6}]
def agrupar_valores_en_conjuntos(lista):
    diccionario = {}
    for diccionario_actual in lista:
        for clave, valor in diccionario_actual.items():
            diccionario[clave].add(valor)
    return diccionario
print(agrupar_valores_en_conjuntos) 

#Ejercicio 4

import csv

def crear_csv(diccionario,archivo):
    with open(archivo,'a',encoding='utf_8',newline='') as archivo:
        archivo.write(['Producto','Valor'])
        for clave,valores in diccionario.items():
            for valor in valores:
                archivo.write([clave,valor])

def leer_csv(archivo):
    resultado={}
    with open(archivo,'r',encoding='utf-8',newline='') as archivo:
        reader=csv.reader(archivo)
        for fila in reader:
            clave=fila[0]
            valor=fila[1]
            if clave in resultado:
                resultado[clave].append(valor)
            else:
                resultado[clave]=[valor]   

#Ejerciicio 5
import csv

libros = [ 
    {"Book": "To Kill A Mockingbird", "Author": "Harper Lee", "Year Released": 1960},
    {"Book": "A Brief History of Time", "Author": "Stephen Hawking", "Year Released": 1988},
    {"Book": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Year Released": 1922},
    {"Book": "The Man Who Mistook His Wife for a Hat", "Author": "Oliver Sacks", "Year Released": 1985},
    {"Book": "Pride and Prejudice", "Author": "Jane Austen", "Year Released": 1813}
]
with open('libros.csv', mode='w', newline='') as archivo:
    campos = ["Book", "Author", "Year Released"]
    write = csv.writer(archivo)
    write.writerow(campos) 

    for libro in libros:
        fila = [libro["Book"], libro["Author"], libro["Year Released"]]
        write.writerow(fila)

seguir = int(("Desea agreagar mas filas(Si=1/No=2)"))
while seguir == 1:
    cantidad = int(input("Cuantos libros desea ingresar"))
    i=0
    while i != cantidad:
        book = input("Ingrese el nombre del Libro")
        Author = input("Ingresere el autor del libro")
        Year_Released = input("Ingrese el anio que fue publicado")
        libro = [book,Author,Year_Released]
        with open(libro.csv, 'a', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(libro)
        i +=1
    seguir = int(("Desea agreagar mas filas(Si=1/No=2)"))
#Ejercicio 6



