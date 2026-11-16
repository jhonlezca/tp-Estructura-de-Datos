from collections import deque

class GrafoJugadores:
    def __init__(self):
        # Lista de adyacencia: { "Nombre Apellido": ["Vecino 1", "Vecino 2"] }
        self.adj = {}
        # Mapa rápido: { "Nombre Apellido": diccionario_u_objeto_jugador }
        self.jugadores_map = {}

    def _obtener_clave(self, j):
        """Extrae 'Nombre Apellido' limpio para usarlo como clave del vértice."""
        if isinstance(j, dict):
            nombre = str(j.get("nombre", "")).strip()
            apellido = str(j.get("apellido", "")).strip()
            return f"{nombre} {apellido}".strip()
        if hasattr(j, "nombre_completo"):
            return str(j.nombre_completo).strip()
        return f"{getattr(j, 'nombre', '')} {getattr(j, 'apellido', '')}".strip()

    def _obtener_edad(self, j):
        """Extrae la edad como entero (int) de forma segura."""
        val = j.get("edad") if isinstance(j, dict) else getattr(j, "edad", None)
        if val is None or val == "":
            return None
        try:
            return int(val)
        except (ValueError, TypeError):
            return None

    def construir_red_cercania_edad(self, lista_jugadores, salto_maximo=1):
        """
        Construye un Grafo No Dirigido donde cada vértice es un jugador ('Nombre Apellido')
        y existe una arista entre dos jugadores si |edad1 - edad2| <= salto_maximo.
        """
        self.adj.clear()
        self.jugadores_map.clear()

        jugadores_validos = []
        for j in lista_jugadores:
            clave = self._obtener_clave(j)
            edad = self._obtener_edad(j)
            if clave and edad is not None:
                self.adj[clave] = []
                self.jugadores_map[clave] = j
                jugadores_validos.append((clave, edad))

        # Crear aristas bidireccionales entre jugadores con edades cercanas
        n = len(jugadores_validos)
        for i in range(n):
            for k in range(i + 1, n):
                clave1, edad1 = jugadores_validos[i]
                clave2, edad2 = jugadores_validos[k]

                if abs(edad1 - edad2) <= salto_maximo:
                    self.adj[clave1].append(clave2)
                    self.adj[clave2].append(clave1)

    def buscar_cercanos_edad_bfs(self, texto_busqueda, max_niveles=2):
        """
        Recorre el grafo en anchura (BFS) usando una Cola (FIFO).
        Agrupa los jugadores alcanzados por nivel de distancia (saltos de edad).
        """
        texto_clean = texto_busqueda.strip().lower()
        
        # Buscar la clave exacta en el grafo (soporta búsqueda parcial o en minúsculas)
        clave_inicio = next(
            (clave for clave in self.adj.keys() if texto_clean in clave.lower()),
            None
        )

        if not clave_inicio:
            return None, {}

        visitados = {clave_inicio}
        cola = deque([(clave_inicio, 0)])  # (clave_actual, nivel_distancia)
        niveles_cercania = {}

        while cola:
            clave_actual, nivel = cola.popleft()  # Extrae el primero que entró (FIFO)

            if nivel > max_niveles:
                continue

            if clave_actual != clave_inicio:
                if nivel not in niveles_cercania:
                    niveles_cercania[nivel] = []
                niveles_cercania[nivel].append(self.jugadores_map[clave_actual])

            # Encolar vecinos directos no visitados
            for clave_vecino in self.adj.get(clave_actual, []):
                if clave_vecino not in visitados:
                    visitados.add(clave_vecino)
                    cola.append((clave_vecino, nivel + 1))

        return clave_inicio, niveles_cercania
    
    def construir_red_posicion(self, lista_jugadores):
        """
        Construye un Grafo No Dirigido conectando a todos los jugadores 
        que comparten la misma posición en la cancha.
        """
        self.adj.clear()
        self.jugadores_map.clear()

        jugadores_validos = []
        for j in lista_jugadores:
            clave = self._obtener_clave(j)
            pos = j.get("posicion") if isinstance(j, dict) else getattr(j, "posicion", None)
            if clave and pos:
                self.adj[clave] = []
                self.jugadores_map[clave] = j
                jugadores_validos.append((clave, str(pos).strip().lower()))

        n = len(jugadores_validos)
        for i in range(n):
            for k in range(i + 1, n):
                clave1, pos1 = jugadores_validos[i]
                clave2, pos2 = jugadores_validos[k]

                if pos1 == pos2:
                    self.adj[clave1].append(clave2)
                    self.adj[clave2].append(clave1)

    def explorar_posicion_dfs(self, texto_busqueda):
        """
        Recorre el grafo en profundidad (DFS) usando Recursión (Pila implícita) 
        para explorar toda la componente conexa de jugadores de esa posición.
        """
        texto_clean = texto_busqueda.strip().lower()
        clave_inicio = next(
            (clave for clave in self.adj.keys() if texto_clean in clave.lower()),
            None
        )

        if not clave_inicio:
            return None, []

        visitados = set()
        comunidad_dfs = []

        def _dfs_recursivo(clave_actual):
            visitados.add(clave_actual)
            comunidad_dfs.append(self.jugadores_map[clave_actual])

            # Profundiza por cada vecino antes de retroceder (backtracking)
            for clave_vecino in self.adj.get(clave_actual, []):
                if clave_vecino not in visitados:
                    _dfs_recursivo(clave_vecino)

        _dfs_recursivo(clave_inicio)
        return clave_inicio, comunidad_dfs