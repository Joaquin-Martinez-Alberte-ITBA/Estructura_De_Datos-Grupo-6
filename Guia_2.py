##Ejercicio 1
str = "cadena de texto123"
letras = sum(char.isalpha() for char in str)
numericos = sum(char.isnumeric() for char in str)
especiales = len(str) - letras - numericos
print(letras)
print(numericos)
print(especiales)

##Ejercicio 2 

str = "contar caracater especifico"
char = 'a'
print(str.count(char))'

##Ejercicio 3

str = "Cambiar a mayus"
print(str.swapcase())'

##Ejercicio 5

str = "Estructura de datos alfa"
lista = str.split()
print(max(lista,key=len))
print(min(lista,key=len))'

#Ejercicio 6

str = "Estructura de datos alfa"
lista = list(set(str))
for a in lista:
    num = 0
    for char in str:
        if char == a:
            num +=1
    print(a,':',num)

#Ejercicio 7

Palabras=["La","materia","Estructuras","de","Datos","es","genial"]
primeraPalabra = 'La'
segundaPalabra = 'es'
diff = Palabras.index(segundaPalabra) - Palabras.index(primeraPalabra)
print(diff)

#Ejercicio 8






