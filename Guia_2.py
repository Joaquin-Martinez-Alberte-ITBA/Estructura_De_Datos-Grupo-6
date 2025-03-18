##Ejercicio 1
'''
str = "cadena de texto123"
letras = sum(char.isalpha() for char in str)
numericos = sum(char.isnumeric() for char in str)
especiales = len(str) - letras - numericos
print(letras)
print(numericos)
print(especiales)
'''
##Ejercicio 2 
'''
str = "contar caracater especifico"
char = 'a'
print(str.count(char))'
'''
##Ejercicio 3
'''
str = "Cambiar a mayus"
print(str.swapcase())'
'''
##Ejercicio 4
str = "Estructura de datos alfa"
lista = str.split()
print(max(lista,key=len))
print(min(lista,key=len))