
class Heap:
    def __init__(self):
        self.heap = []


    def insertar(self, dato):
        self.heap.append(dato)
        i = len(self.heap) - 1

        self._flotar(i)

    # flota el elemento en el índice dado hacia arriba hasta que se cumpla la propiedad del min-heap
    def _flotar(self, indice):
        while indice > 0 and self.heap[indice][1] < self.heap[(indice - 1) // 2][1]:
            padre = (indice - 1) // 2
            self.heap[indice], self.heap[padre] = (self.heap[padre], self.heap[indice])
            indice = padre
    


    def obtener_minimo(self):
        if not self.heap:
            return None
        return self.heap[0]

    
    # devuelve una lista con los n elementos más grandes del heap
    
    def _hundir(self, indice, heap):
        n = len(heap)
        while True:
            izquierdo = 2 * indice + 1
            derecho = 2 * indice + 2
            menor = indice

            if izquierdo < n and heap[izquierdo][1] < heap[menor][1]:
                menor = izquierdo
            if derecho < n and heap[derecho][1] < heap[menor][1]:
                menor = derecho

            if menor == indice:
                break

            heap[indice], heap[menor] = heap[menor], heap[indice]
            indice = menor

    def _eliminar_minimo(self, heap):
        if not heap:
            return None
        minimo = heap[0]
        
        if len(heap) == 1:
            heap.pop()
            return minimo
    
      
        heap[0] = heap[-1]
        heap.pop()
        self._hundir(0, heap)

        return minimo
    
    def obtener_n_mas_pequenos(self, n):
        if n <= 0:
            return []
        if n > len(self.heap):
            n = len(self.heap)

        # Crear una copia del heap para no modificar el original
        copia_heap = self.heap[:]
        resultado = []

        for _ in range(n):
            minimo =  self._eliminar_minimo(copia_heap)
            resultado.append(minimo)
           

        return resultado        
       

    




