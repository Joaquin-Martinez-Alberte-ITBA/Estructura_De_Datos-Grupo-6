class Nodo:
    def __init__(self,dato,sig=None):
        self.dato=dato
        
        self.sig=sig
        
    def __str__(self):
        siguiente=self.sig.dato if self.sig else None
        return f'{self.dato} y me sigue {siguiente}'

if __name__=="__main__":
    nodo1=Nodo(1)
    nodo2=Nodo(2)
    nodo3=Nodo(3)
    nodo4=Nodo(4)
    nodo1.sig=nodo2
    nodo2.sig=nodo3
    nodo3.sig=nodo4
    print(nodo1)
    print(nodo2)

    actual=nodo1
    while actual !=None:
        print(actual)
        actual=actual.sig

   