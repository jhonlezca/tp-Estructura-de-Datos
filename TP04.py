# Generar casos donde el BST del TP3 quede desbalanceado (ej: insertar datos ya ordenados).
# Implementar AVL con las rotaciones correspondientes.




class NodoAVL:
    def __init__(self, equipo):
        self.equipo = equipo        # Objeto o dict del equipo
        self.clave = equipo["nombre"].strip().lower()  # Clave de ordenamiento
        self.izquierdo = None
        self.derecho = None
        self.altura = 0

# Tercer paso: ahora vamos a crear la clase del Arbol. A tener en cuenta: vamos a utilizar una lista desordenada de los equipos (la vamos a desordenar aparte) para no terminar en un arbol vertical descendente.

class ArbolAVL:
    def __init__(self):
        self.raiz = None


    def altura(self, nodo):
            if nodo.altura is None:
                return -1  # Altura de un nodo nulo es -1
            else:
                return nodo.altura
    
    def actualizar_altura(self, nodo):
        if nodo is not None:
            altura_izq = self.altura(nodo.izquierdo)
            altura_der = self.altura(nodo.derecho)
            nodo.altura = 1 + max(altura_izq, altura_der)

    def rotar_simple(self,nodo, control):
        if control:
            aux = nodo.izquierdo
            nodo.izquierdo = aux.derecho
            aux.derecho = nodo
        else:
            aux = nodo.derecho
            nodo.derecho = aux.izquierdo
            aux.izquierdo = nodo
        self.actualizar_altura(nodo)
        self.actualizar_altura(aux)
        nodo = aux
        return nodo

    def rotar_Doble(self,nodo,control):
        if control:
            nodo.izquierdo = self.rotar_simple(nodo.izquierdo, False)
            nodo = self.rotar_simple(nodo, True)
        else:
            nodo.derecho = self.rotar_simple(nodo.derecho, True)
            nodo = self.rotar_simple(nodo, False)
        return nodo


    def balancear(self, nodo):
        if nodo is not None:
            self.actualizar_altura(nodo)
            balance = self.altura(nodo.izquierdo) - self.altura(nodo.derecho)

            if balance > 1:  # Desbalance a la izquierda
                if self.altura(nodo.izquierdo.izquierdo) >= self.altura(nodo.izquierdo.derecho):
                    nodo = self.rotar_simple(nodo, True)  # Rotación simple a la derecha
                else:
                    nodo = self.rotar_Doble(nodo, True)  # Rotación doble a la derecha
            elif balance < -1:  # Desbalance a la derecha
                if self.altura(nodo.derecho.derecho) >= self.altura(nodo.derecho.izquierdo):
                    nodo = self.rotar_simple(nodo, False)  # Rotación simple a la izquierda
                else:
                    nodo = self.rotar_Doble(nodo, False)  # Rotación doble a la izquierda

        return nodo

    def insertarNodo_AVL(self, nodo_actual, equipo):
        if nodo_actual is None:
            return NodoAVL(equipo)

        clave = equipo["nombre"].strip().lower()

        if clave < nodo_actual.clave:
            nodo_actual.izquierdo = self.insertarNodo_AVL(nodo_actual.izquierdo, equipo)
        elif clave > nodo_actual.clave:
            nodo_actual.derecho = self.insertarNodo_AVL(nodo_actual.derecho, equipo)
        else:
            # Si la clave ya existe, no hacemos nada (no se permiten duplicados)
            return nodo_actual

        # Balanceamos el árbol después de la inserción
        nodo_actual = self.balancear(nodo_actual)
        return nodo_actual

    def eliminarNodo_AVL(self, nodo_actual, clave):
        if nodo_actual is None:
            return None

        # Paso 1: búsqueda del nodo a eliminar
        if clave < nodo_actual.clave:
            nodo_actual.izquierdo = self.eliminarNodo_AVL(nodo_actual.izquierdo, clave)
        elif clave > nodo_actual.clave:
            nodo_actual.derecho = self.eliminarNodo_AVL(nodo_actual.derecho, clave)
        else:
            # Caso encontrado
            if nodo_actual.izquierdo is None:
                return nodo_actual.derecho
            elif nodo_actual.derecho is None:
                return nodo_actual.izquierdo
            else:
                # Caso con dos hijos: buscar sucesor (mínimo en subárbol derecho)
                sucesor = self._minimo(nodo_actual.derecho)
                nodo_actual.equipo = sucesor.equipo
                nodo_actual.clave = sucesor.clave
                nodo_actual.derecho = self.eliminarNodo_AVL(nodo_actual.derecho, sucesor.clave)

        # Paso 2: balancear después de la eliminación
        nodo_actual = self.balancear(nodo_actual)
        return nodo_actual



# Cuarto paso: definimos la busqueda. 

# --- BÚSQUEDA ---
    def buscar(self, nombre_equipo):
        """Busca un equipo por nombre en el árbol."""
        clave = nombre_equipo.strip().lower()
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo_actual, clave):
        if nodo_actual is None or nodo_actual.clave == clave:
            return nodo_actual.equipo if nodo_actual else None

        if clave < nodo_actual.clave:
            return self._buscar_recursivo(nodo_actual.izquierdo, clave)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, clave)


# --- RECORRIDOS (Inorder, Preorder, Postorder) ---
    def recorrido_inorder(self):
        """Inorder (Izq - Raíz - Der): Devuelve los equipos ordenados alfabéticamente."""
        resultados = []
        self._inorder_recursivo(self.raiz, resultados)
        return resultados

    def _inorder_recursivo(self, nodo, resultados):
        if nodo:
            self._inorder_recursivo(nodo.izquierdo, resultados)
            resultados.append(nodo.equipo)
            self._inorder_recursivo(nodo.derecho, resultados)

# Agregamos los recorridos (Inorder, Preorder, Postorder)

    def recorrido_preorder(self):
        """Preorder (Raíz - Izq - Der): Muestra la estructura jerárquica."""
        resultados = []
        self._preorder_recursivo(self.raiz, resultados)
        return resultados

    def _preorder_recursivo(self, nodo, resultados):
        if nodo:
            resultados.append(nodo.equipo)
            self._preorder_recursivo(nodo.izquierdo, resultados)
            self._preorder_recursivo(nodo.derecho, resultados)

    def recorrido_postorder(self):
        """Postorder (Izq - Der - Raíz)."""
        resultados = []
        self._postorder_recursivo(self.raiz, resultados)
        return resultados

    def _postorder_recursivo(self, nodo, resultados):

        if nodo:
            self._postorder_recursivo(nodo.izquierdo, resultados)
            self._postorder_recursivo(nodo.derecho, resultados)
            resultados.append(nodo.equipo)






# Comparar BST común vs. AVL en esos casos de desbalance.

"""Operación	BST desbalanceado	AVL
    Altura	    ≈ n	                ≈ log n
    Búsqueda	O(n)	            O(log n)
    Inserción	O(n)	            O(log n)
    Eliminación	O(n)	            O(log n)
"""
# Explicar por qué el balance importa (relación con la complejidad O(log n) vs O(n)).
"""
En un BST desbalanceado, las operaciones se degradan a O(n) porque el árbol se convierte en una lista.

En un AVL, el balance garantiza que la altura se mantenga en O(log n), 
preservando la eficiencia de las operaciones de búsqueda, inserción y eliminación.

"""

