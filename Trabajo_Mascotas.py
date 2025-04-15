class Mascota:
    def __init__(self, nombre, identificador, tipo, edad, disponible=True):
        self.nombre = nombre
        self.identificador = identificador
        self.tipo = tipo
        self.edad = edad
        self.disponible = disponible

    def adoptar_mascota(self):
        self.disponible = False

    def ver_informacion(self):
        return {
            "Nombre": self.nombre,
            "ID": self.identificador,
            "Tipo": self.tipo,
            "Edad": self.edad,
            "Disponible": self.disponible
        }
class Adoptante:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.historial_adopciones = []

    def registrar_adopcion(self, adopcion):
        self.historial_adopciones.append(adopcion)

    def consultar_adopciones(self):
        return self.historial_adopciones

    def ver_informacion(self):
        return {
            "Nombre": self.nombre,
            "DNI": self.dni,
            "Cantidad de adopciones": len(self.historial_adopciones)
        }
class Adopcion:
    def __init__(self, id_adopcion, adoptante, mascota, fecha_adopcion):
        self.id_adopcion = id_adopcion
        self.adoptante = adoptante
        self.mascota = mascota
        self.fecha_adopcion = fecha_adopcion

    def consultar_adopcion(self):
        return {
            "ID Adopción": self.id_adopcion,
            "Adoptante": self.adoptante.nombre,
            "Mascota": self.mascota.nombre,
            "Fecha": self.fecha_adopcion
        }
class Refugio:
    def __init__(self, nombre, nit, direccion):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.mascotas = []
        self.adoptantes = []
        self.adopciones = []

    # Mascotas
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def eliminar_mascota(self, identificador):
        self.mascotas = [m for m in self.mascotas if m.identificador != identificador]

    def buscar_mascota(self, identificador):
        return next((m for m in self.mascotas if m.identificador == identificador), None)

    # Adoptantes
    def agregar_adoptante(self, adoptante):
        self.adoptantes.append(adoptante)

    def buscar_adoptante(self, dni):
        return next((a for a in self.adoptantes if a.dni == dni), None)

    # Adopciones
    def registrar_adopcion(self, id_adopcion, dni, identificador_mascota, fecha):
        adoptante = self.buscar_adoptante(dni)
        mascota = self.buscar_mascota(identificador_mascota)
        if adoptante and mascota and mascota.disponible:
            mascota.adoptar_mascota()
            adopcion = Adopcion(id_adopcion, adoptante, mascota, fecha)
            adoptante.registrar_adopcion(adopcion)
            self.adopciones.append(adopcion)
            return adopcion
        else:
            raise Exception("Adopción no válida")

    # Consultas
    def consultar_mascotas_disponibles(self):
        return [m.ver_informacion() for m in self.mascotas if m.disponible]

    def consultar_adoptantes(self):
        return [a.ver_informacion() for a in self.adoptantes]

    def consultar_adopciones(self):
        return [a.consultar_adopcion() for a in self.adopciones]
