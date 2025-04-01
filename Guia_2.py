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
##Ejercicio 5
'''
str = "Estructura de datos alfa"
lista = str.split()
print(max(lista,key=len))
print(min(lista,key=len))'
'''
#Ejercicio 6
'''
str = "Estructura de datos alfa"
lista = list(set(str))
for a in lista:
    num = 0
    for char in str:
        if char == a:
            num +=1
    print(a,':',num)
'''
#Ejercicio 7
'''
Palabras=["La","materia","Estructuras","de","Datos","es","genial"]
primeraPalabra = 'La'
segundaPalabra = 'es'
diff = Palabras.index(segundaPalabra) - Palabras.index(primeraPalabra)
print(diff)
'''
#Ejercicio 8
'''
def comprimir_y_revertir(cadena):
    if not cadena:
        return ""
    comp = ""
    count = 1
    for i in range(1, len(cadena)):
        if cadena[i] == cadena[i-1]:
            count += 1
        else:
            comp += cadena[i-1] + format(count, 'x')
            count = 1
    comp += cadena[-1] + format(count, 'x')
    return comp[::-1]
entrada = "aaaaaaaaaaa"
resultado = comprimir_y_revertir(entrada)
print(resultado)  '
'''
#Ejercicio 9
def reducir_cadena(cadena, k):
    stack = []
    for char in cadena:
        if stack and stack[-1][0] == char:
            contador = stack[-1][1] + 1
            stack[-1] = (char, contador)
            if contador == k:
                stack.pop()
        else:
            stack.append((char, 1))
    resultado = "".join(char * contador for char, contador in stack)
    return resultado
cadena_entrada = "esteeparaestee"
k = 2
resultado = reducir_cadena(cadena_entrada, k)
print(resultado) 

        
    









