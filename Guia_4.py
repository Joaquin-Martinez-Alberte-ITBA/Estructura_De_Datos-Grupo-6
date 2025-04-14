#EJERCICIO 1
class Camion:
    lista_camiones = []
    lista_patentes = []
    lista_anios = []
    def __init__(self, patente, carga, marca, anio):
        if patente in Camion.lista_patentes:
            raise ValueError(f"Error: La patente '{patente}' ya está en uso.")
        self.patente = patente
        self.carga = carga
        self.marca = marca
        self.anio = anio
        Camion.lista_camiones.append(self)
        Camion.lista_patentes.append(patente)
        Camion.lista_anios.append(anio)

    def __str__(self) -> str:
        return f'''Camion #{self.patente}\nCarga: {self.carga}\n
        Marca: {self.marca}\nAño: {self.anio} '''
    
    def __eq__(self, other):
        return (self.patente == other.patente)
    
    def setcarga(self, carga):
        if isinstance(carga,float) and carga >0:
            self.carga=carga
            return True
        else: 
            return False
    @classmethod
    def antiguedad(cls):
        camiones=cls.lista_camiones
        camiones.sort(lambda x : x.anio)
        for camion in camiones:
            print(camion)
            
    @classmethod
    def purgar(cls):
        resultado = []
        patentes_vistas = []
        for camion in cls.lista_camiones:
            if camion.patente not in patentes_vistas:
                resultado.append(camion)
                patentes_vistas.append(camion.patente)
        cls.lista_camiones = resultado
        cls.lista_patentes = patentes_vistas
        return cls.lista_camiones
    @classmethod
    def marcas_usadas(cls):
        lista=[]
        for camion in cls.lista_camiones:
            encontrado=False
            for sublista in lista:
                if sublista[0] == camion.marca:
                    encontrado=True
                    sublista[1]+=1
            if encontrado==False:
                lista.append([camion.marca,0])   
        lista.sort(lambda x : x[1])
        return lista[-1]        
            
        
def menu_camion():
    while True:
        print('''\nElija una opción:
a) Registrar un nuevo camión
b) Modificar la carga de un camión
c) Mostrar camiones del más antiguo al más nuevo
d) Mostrar la marca más registrada
e) Salir''')

        eleccion = input('Su elección: ').lower()

        if eleccion == 'a':
            patente = input('Ingrese una patente sin espacios: ').strip().upper()
            while len(patente) not in (6, 8):
                patente = input('Patente inválida. Reingrese: ').strip().upper()

            try:
                carga = float(input('Ingrese la carga del camión (kg): '))
                while carga <= 0:
                    carga = float(input('Carga inválida. Reingrese: '))
            except ValueError:
                print("Debe ingresar un número válido.")
                continue

            marca = input('Ingrese la marca del camión: ').strip().title()
            while not marca:
                marca = input('Marca inválida. Reingrese: ').strip().title()

            try:
                anio = int(input('Ingrese el año del camión: '))
                while anio <= 0:
                    anio = int(input('Año inválido. Reingrese: '))
            except ValueError:
                print("Debe ingresar un año válido.")
                continue

            try:
                Camion(patente, carga, marca, anio)
                print("Camión registrado con éxito.")
            except ValueError as e:
                print(e)

        elif eleccion == 'b':
            patente = input("Ingrese la patente del camión a modificar: ").strip().upper()
            encontrados = [c for c in Camion.lista_camiones if c.patente == patente]
            if not encontrados:
                print("Camión no encontrado.")
            else:
                try:
                    nueva_carga = float(input("Nueva carga (kg): "))
                    if encontrados[0].setcarga(nueva_carga):
                        print("Carga modificada con éxito.")
                    else:
                        print("Carga inválida.")
                except ValueError:
                    print("Debe ingresar un número válido.")

        elif eleccion == 'c':
            print("\nLista de camiones (ordenados por antigüedad):")
            Camion.antiguedad()

        elif eleccion == 'd':
            marca_top = Camion.marcas_usadas()
            if marca_top:
                print(f"La marca más registrada es {marca_top[0]} ({marca_top[1] + 1} veces)")
            else:
                print("No hay camiones registrados.")

        elif eleccion == 'e':
            print("Saliendo del menú...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


menu_camion()

#EJERCICIO 2
#a) y b) y d)
class Computadora():
    cantidad_creadas = 0 

    def __init__(self, marca="Genérica", modelo="Base", sistema_operativo="Windows 10", 
                 ram=8, almacenamiento=256, procesador="Intel i5", fecha_compra="2023-01-01"):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.ram = ram 
        self.almacenamiento = almacenamiento
        self.procesador = procesador
        self.fecha_compra = fecha_compra

        Computadora.cantidad_creadas += 1

    def __str__(self):
        return (f"Computadora {self.marca} {self.modelo} - {self.procesador}\n"
                f"SO: {self.sistema_operativo} | RAM: {self.ram}GB | Almacenamiento: {self.almacenamiento}GB\n"
                f"Fecha de compra: {self.fecha_compra}")
    
    def addRAM(self, cantidad):
        if cantidad > 0:
            self.ram += cantidad
            print(f"Se agregaron {cantidad} GB de RAM. RAM total: {self.ram} GB.")
        else:
            print("La cantidad debe ser positiva.")
    def getCapacity(self, componente):
        componente = componente.lower()
        if componente == "ram":
            print(f"RAM instalada: {self.ram} GB")
        elif componente == "almacenamiento":
            print(f"Almacenamiento total: {self.almacenamiento} GB")
        else:
            print("Componente no reconocido. Use 'ram' o 'almacenamiento'.")



#c) 
pc1 = Computadora("HP", "Pavilion", "Windows 11", 16, 512, "Intel i7", "2024-01-15")
pc2 = Computadora("Lenovo", "ThinkPad", "Ubuntu 22.04", 8, 256, "AMD Ryzen 5", "2023-07-10")
pc3 = Computadora()

print(pc1)
print(pc2)
print(pc3)


