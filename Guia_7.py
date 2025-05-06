from claseNodo import Nodo
from lista import Lista
#Parte 1

class Camion:
    lista_camiones = Lista()
    lista_patentes = Lista()
    lista_anios = Lista()
    def __init__(self, patente, carga, marca, anio):
        if patente in Camion.lista_patentes:
            raise ValueError(f"Error: La patente '{patente}' ya está en uso.")
        self.patente = patente
        self.carga = carga
        self.marca = marca
        self.anio = anio
        Camion.lista_camiones.agregarNodoAlInicio(self)
        Camion.lista_patentes.agregarNodoAlInicio(patente)
        Camion.lista_anios.agregarNodoAlInicio(anio)

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