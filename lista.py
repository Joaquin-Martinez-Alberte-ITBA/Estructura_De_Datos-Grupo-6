from claseNodo import *

class Lista():
    def __init__(self, inicio=None):
        self.inicio=inicio
    
    def agregarNodoAlInicio(self,nodo):
        #Didactico
        if self.inicio==None:
            self.inicio=nodo
        else:
            nodo.sig=self.inicio
            self.inicio=nodo
        #Eficiente
        # nodo.sig=self.inicio
        # self.inicio=nodo
    
    def agregarNodoAlFinal(self,nodo):
        if self.inicio==None:
            self.inicio=nodo
        else:
            mover=self.inicio
            while mover.sig!=None:
                mover=mover.sig
            mover.sig=nodo
    
    def mostrarLista(self):
        nodo=self.inicio
        if not nodo:
            print('lista vacia')
        else:
            while nodo!=None:
                print(nodo)
                nodo=nodo.sig
    
    def buscarDato(self,num):
        buscar=self.inicio
        
        while buscar!=None:
            if buscar.dato==num:
                return True
            else:
                buscar=buscar.sig
        return False
    
    def eliminar(self, num):
        if self.buscarDato(num):
            actual = self.inicio
            previo = None
            while actual != None:
                if actual.dato == num:
                    if previo == None:
                        self.inicio = actual.sig
                    else:
                        previo.sig = actual.sig
                    print('El nodo ha sido eliminado')
                    actual = None  # salir del bucle
                else:
                    previo = actual
                    actual = actual.sig
        else:
            print('No existe, no se puede eliminar')

if __name__ == "__main__":
    # Crear lista
    lista = Lista()

    # Agregar nodos
    lista.agregarNodoAlInicio(Nodo(3))
    lista.agregarNodoAlInicio(Nodo(2))
    lista.agregarNodoAlFinal(Nodo(4))
    lista.agregarNodoAlFinal(Nodo(5))

    print("\nLista actual:")
    lista.mostrarLista()

    # Buscar un dato
    print("\nBuscando el número 4:")
    encontrado = lista.buscarDato(4)
    print("Encontrado:", encontrado)

    print("\nBuscando el número 10:")
    encontrado = lista.buscarDato(10)
    print("Encontrado:", encontrado)

    # Eliminar un dato
    print("\nEliminando el número 2:")
    lista.eliminar(2)
    lista.mostrarLista()

    print("\nEliminando el número 10 (que no existe):")
    lista.eliminar(10)
    lista.mostrarLista()