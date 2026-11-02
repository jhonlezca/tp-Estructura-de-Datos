class GrafoEdades:
    def __init__(self, rango_diferencia=2):
        # { jugador: { jugador_vecino: diferencia_edad } }
        self.adj = {}
        self.rango_diferencia = rango_diferencia

    def construir_grafo(self, lista_jugadores):
        """Construye las conexiones entre jugadores basándose solo en la edad."""
        self.adj.clear()
        
        # 1. Agregar todos los nodos
        for jug in lista_jugadores:
            if jug.edad is not None:  # Validar que tenga la edad cargada
                self.adj[jug] = {}

        nodos = list(self.adj.keys())
        n = len(nodos)

        # 2. Conectar jugadores cuya diferencia de edad sea <= rango_diferencia
        for i in range(n):
            for j in range(i + 1, n):
                j1 = nodos[i]
                j2 = nodos[j]

                diferencia = abs(j1.edad - j2.edad)

                if diferencia <= self.rango_diferencia:
                    # Guardamos la diferencia como peso de la arista
                    self.adj[j1][j2] = diferencia
                    self.adj[j2][j1] = diferencia

    def obtener_jugadores_de_edad_similar(self, jugador_buscado):
        """Retorna los jugadores conectados al jugador dado, ordenados por cercanía de edad."""
        if jugador_buscado not in self.adj:
            return []

        vecinos = self.adj[jugador_buscado]
        # Ordenamos por menor diferencia de edad (peso)
        return sorted(vecinos.items(), key=lambda x: x[1])

    def buscar_por_rango_edad(self, edad_min, edad_max):
        """Filtra y devuelve todos los jugadores en el subgrafo de ese rango."""
        return [j for j in self.adj.keys() if edad_min <= j.edad <= edad_max]