###Ejercicio 1
'''
num1 = 4
num2 = 6
operador = '*'
if operador == '*':
    final =num1*num2
if operador == '+':
    final = num1 +num2
if operador == '-':
    final = num1 - num2
if operador == '/':
    try:
        final=num1/num2
    except ZeroDivisionError as e:
        print(f'{e} Vuelve a ingresar el numero 2, no puede ser 0')
'''
### Ejercicio 2
import csv

def cargar_materias(archivo):
    materias = []
    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Saltar encabezado
            for row in reader:
                materias.append((row[0], row[1]))  # (Nombre, Carga horaria)
    except FileNotFoundError:
        print("Error: Archivo de materias no encontrado.")
        exit(1)
    return materias

materias = cargar_materias("materias.csv")

def mostrar_materias():
    print("Materias disponibles:")
    for i, (materia, carga) in enumerate(materias):
        print(f"{i}. {materia} - {carga} horas")

def matricular_materia(materias_inscritas):
    try:
        indice = int(input("Ingrese el índice de la materia a matricularse: "))
        if indice < 0 or indice >= len(materias):
            raise ValueError("Índice inválido. No existe la materia seleccionada.")
        if materias[indice][0] in [m[0] for m in materias_inscritas]:
            print("Ya estás inscrito en esta materia.")
        else:
            materias_inscritas.append(materias[indice])
            print(f"Te has inscrito en {materias[indice][0]}")
    except ValueError as e:
        print(f"Error: {e}. Ingrese un número válido.")

def ver_materias_inscritas(materias_inscritas):
    """Muestra las materias en las que el usuario está inscrito."""
    if not materias_inscritas:
        print("No estás inscrito en ninguna materia.")
    else:
        print("Materias inscritas:")
        for i, (materia, carga) in enumerate(materias_inscritas):
            print(f"{i}. {materia} - {carga} horas")

def confirmar_inscripcion(materias_inscritas):
    if not materias_inscritas:
        print("No hay materias para confirmar.")
    else:
        print("Inscripción confirmada en las siguientes materias:")
        for materia, carga in materias_inscritas:
            print(f"- {materia} ({carga} horas)")
        print("Inscripción completada.")
        exit(0)

def menu():
    materias_inscritas = []
    while True:
        print("\n--- Sistema de Matriculación ---")
        print("a. Ver materias disponibles")
        print("b. Matricularse a una nueva materia")
        print("c. Ver materias inscritas")
        print("d. Confirmar inscripción")
        
        opcion = input("Seleccione una opción: ").strip().lower()
        if opcion == 'a':
            mostrar_materias()
        elif opcion == 'b':
            matricular_materia(materias_inscritas)
        elif opcion == 'c':
            ver_materias_inscritas(materias_inscritas)
        elif opcion == 'd':
            confirmar_inscripcion(materias_inscritas)
        else:
            print("Opción inválida. Intente de nuevo.")