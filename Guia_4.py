#EJERCICIO 1
class Camion:
    lista_patentes = []
    def __init__(self, patente, carga, marca, anio):
        if patente in Camion.lista_patentes:
            raise ValueError(f"Error: La patente '{patente}' ya está en uso.")
        self.patente = patente
        self.carga = carga
        self.marca = marca
        self.anio = anio
        Camion.lista_patentes.append(patente)

    def __str__(self) -> str:
        return f'''Camion #{self.patente}\nCarga: {self.carga}\n
        Marca: {self.marca}\nAño: {self.anio} '''
    
    def __eq__(self, other):
        return (self.patente == other.patente)
furgon1 = Camion("ABC123", "1500 kg", "Mercedes-Benz", 2020)
furgon2 = furgon1  # Mismo objeto que furgon1
furgon3 = Camion("XYZ789", "2000 kg", "Ford", 2022)
furgon4 = Camion("LMN456", "1800 kg", "Iveco", 2021)

print(furgon1 == furgon2)
print(furgon3 is furgon4)
print(furgon3 == furgon4)
print(furgon3 is furgon4)

#EJERCICIO 2