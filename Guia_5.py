###Ejercicio 1 
'''
class Vehiculo:
    lista_patentes = []

    def __init__(self, patente, marca, anio,tipo_vehiculo):
        if patente in Vehiculo.lista_patentes:
            raise ValueError(f"Error: La patente '{patente}' ya está en uso.")
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.posicion = 0
        self.tipo_vehiculo = tipo_vehiculo
        Vehiculo.lista_patentes.append(patente)

    def trasladarse(self, desplazamiento):
        self.posicion += desplazamiento
        print(f"{self.__class__.__name__} con patente {self.patente} se trasladó {desplazamiento} unidades. Nueva posición: {self.posicion}")

    def descripcion(self):
        return f"{self.__class__.__name__} - Patente: {self.patente}, Marca: {self.marca}, Año: {self.anio}, Posición: {self.posicion}"


class Camion(Vehiculo):
    def __init__(self, patente, marca, anio, carga):
        super().__init__(patente, marca, anio)
        self.carga = carga
        self.ruedas = 8

    def descripcion(self):
        base = super().descripcion()
        return f"{base}, Ruedas: {self.ruedas}, Carga: {self.carga}kg"


class Auto(Vehiculo):
    def __init__(self, patente, marca, anio):
        super().__init__(patente, marca, anio)
        self.ruedas = 4

    def descripcion(self):
        base = super().descripcion()
        return f"{base}, Ruedas: {self.ruedas}"
    
class Lancha(Vehiculo):
    def __init__(self, marca, anio,marca_motor,rei,tipo):
        super().__init__(marca, anio)
        self.rei = rei
        self.marca_motor = marca_motor
        self.tipo = tipo
    def trasladarse(self, desplazamiento):
        self.posicion += desplazamiento
        print(f"Se dezplaza por agua a {self.tipo} a la posicion {desplazamiento}")

class Velero(Lancha):
    def __init__(self,marca,anio,rei,cant_velas,tipo):
        super().__init__(marca, anio,rei,tipo)
        self.cant_velas = cant_velas

class Anfibio(Vehiculo):
    def __init__(self, marca, anio,marca_motor):
        super().__init__(marca, anio)
        self.marca_motor = marca_motor

    def trasladarse_por_agua(self, desplazamiento):
        self.posicion += desplazamiento
        print(f"Se dezplaza por agua a agua a la posicion {desplazamiento}")
'''
###Ejercicio 3

    