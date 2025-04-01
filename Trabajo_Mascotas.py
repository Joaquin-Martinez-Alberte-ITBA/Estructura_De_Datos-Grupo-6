class Mascota():
    def __init__(self, Nombre:str, id:str, Tipo:str, edad:int, disponibilidad:str):
        self.Nombre = Nombre
        self.id = id
        self.Tipo = Tipo
        self.edad = edad
        self.disponibilidad = disponibilidad
        

class Refugio():
    def __init__(self, Nombre:str, direccion:str, mascotas =[], adoptantes = [], adopciones = [] ):
        self.nombre = Nombre
        self.setnit()
        self.direccion = direccion
        self.mascotas = mascotas
        self.adoptantes = adoptantes
        self.adopciones = adopciones
    def setnit(self):
        NIT = input('Ingrese NIT: ')
        while len(NIT) != 10 or NIT.isalpha() == False:
            NIT = input('Ingreso incorrecto: ')
        self.NIT = NIT
    def getnit(self):
        return self.NIT
    def __str__(self):
        return f'{self.nombre} con NIT: {self.NIT}'
    def agregarMacotas(self):
        nombremascota = input('Ingrese un nombre mascota: ')
        idinput = input('Ingrese un id: ')
        tipoinput = input('Ingrese el tipo de mascota: ')
        edadinput = input('Ingrese una edad: ')
        confirmacioninput = input('Ingrese disponibilidad de mascota: ')
        self.mascotas.append(Mascota(nombremascota, idinput, tipoinput, edadinput, confirmacioninput))
        
        print(f'se agrego exitosamente la mascota. Lista de mascotas {self.mascotas}')
    
    
refugio1 = Refugio('refugio 1', 'San Martin 200')
print(refugio1)