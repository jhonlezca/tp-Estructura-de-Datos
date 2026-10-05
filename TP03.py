# TP 03: Arbol Binario de Busqueda

# Incorporar un árbol binario para resolver una necesidad real del proyecto (típicamente, búsqueda ordenada).

# 1) Definir la clave de ordenamiento (¿por título? ¿por rating? ¿por año?).

# 2) Implementar inserción, búsqueda y recorridos (inorder, preorder, postorder).

# 3) Integrar el árbol a una funcionalidad real de la app (no un árbol "de juguete" aislado).

# 4) Comparar contra la búsqueda secuencial del TP2.

# Primer paso: definimos la clave de ordenamiento. En nuestro caso, elegimos el nombre del equipo convertido a minusculas. El motivo es que nos permite reemplazar o mejorar directamente la busqueda binaria y lineal en listas del TP 02.

# Segundo paso: Para trabajar con un arbol de busqueda binaria vamos a necesitar dos clases: el Nodo y el Arbol. Primero vamos a crear la clase Nodo. Esta va a almacenar al objeto Equipo y las referencias a sus hijos (izquierda y derecha).

class Nodo:
    def __init__(self, equipo):
        self.equipo = equipo        # Objeto o dict del equipo
        self.clave = equipo["nombre"].strip().lower()  # Clave de ordenamiento
        self.izquierdo = None
        self.derecho = None
        

# Tercer paso: ahora vamos a crear la clase del Arbol. A tener en cuenta: vamos a utilizar una lista desordenada de los equipos (la vamos a desordenar aparte) para no terminar en un arbol vertical descendente.

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

# Definimos la insercion individual de los equipos en el arbol.

    def insertar(self, equipo):
        """
        Inserta un nuevo equipo en el árbol comparando su clave alfabética.
        """
        if self.raiz is None:
            self.raiz = Nodo(equipo)
        else:
            self._insertar_recursivo(self.raiz, equipo)

    def _insertar_recursivo(self, nodo_actual, equipo):
        clave = equipo["nombre"].strip().lower()

        if clave < nodo_actual.clave:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(equipo)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, equipo)
        elif clave > nodo_actual.clave:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(equipo)
            else:
                self._insertar_recursivo(nodo_actual.derecho, equipo)

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