
class Heap:
    def __init__(self):
        self.heap = []


    def insertar(self, dato):
        self.heap.append(dato)
        i = len(self.heap) - 1

        self._flotar(i)

    # flota el elemento en el índice dado hacia arriba hasta que se cumpla la propiedad del min-heap
    def _flotar(self, indice):
        while indice > 0 and self.heap[indice] < self.heap[(indice - 1) // 2]:
            padre = (indice - 1) // 2
            self.heap[indice], self.heap[padre] = (self.heap[padre], self.heap[indice])
            indice = padre
    


    def obtener_maximo(self):
        if not self.heap:
            return None
        return self.heap[0]

    
    # devuelve una lista con los n elementos más grandes del heap
    def topN(self, n):
        top = []
        
        if n < len(self.heap):
            for i in range(n):
                top.append(self.heap[i])
            return top
        else:
            print("El valor de n es mayor que la cantidad de elementos en el heap.")
        
       
            




    




