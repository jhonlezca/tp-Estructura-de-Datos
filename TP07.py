class GrafoFiltroAtributo:
    def __init__(self):
        # Lista de adyacencia: { id_jugador: [lista_de_ids_conectados] }
        self.adj = {}
        # Mapa id_jugador -> Objeto/Diccionario completo de Jugador
        self.jugadores_map = {}

    def construir_subgrafo_por_atributo(self, lista_jugadores, atributo, valor_buscado):
        """
        Filtra los jugadores que cumplen con 'atributo == valor_buscado'
        y construye las aristas entre todos los que comparten dicho criterio.
        """
        self.adj.clear()
        self.jugadores_map.clear()

        jugadores_filtrados = []
        valor_buscado_clean = str(valor_buscado).strip().lower()

        # 1. Filtrar los nodos según el atributo y su valor
        for j in lista_jugadores:
            # Obtención adaptable según si 'j' es un diccionario o un Objeto Jugador
            if isinstance(j, dict):
                val = j.get(atributo)
            else:
                val = getattr(j, atributo, None)

            if val is None:
                continue

            # Comparación específica para números (edad) o cadenas de texto (posicion/nacionalidad)
            if atributo == "edad":
                try:
                    if int(val) == int(valor_buscado):
                        jugadores_filtrados.append(j)
                except (ValueError, TypeError):
                    continue
            else:
                if str(val).strip().lower() == valor_buscado_clean:
                    jugadores_filtrados.append(j)

        # 2. Registrar los nodos filtrados en la lista de adyacencia
        for j in jugadores_filtrados:
            if isinstance(j, dict):
                id_j = j.get("id_jugador") or f"{j.get('nombre')}_{j.get('apellido')}"
            else:
                id_j = getattr(j, "id_jugador", getattr(j, "nombre_completo", str(j)))

            self.adj[id_j] = []
            self.jugadores_map[id_j] = j

        # 3. Crear aristas bidireccionales (Grafo No Dirigido / Componente Conexa)
        ids = list(self.adj.keys())
        n = len(ids)
        for i in range(n):
            for k in range(i + 1, n):
                id1 = ids[i]
                id2 = ids[k]
                self.adj[id1].append(id2)
                self.adj[id2].append(id1)

    def obtener_red_filtrada(self):
        """Devuelve una lista de tuplas: (jugador, cantidad_de_conexiones)"""
        resultados = []
        for id_j, vecinos in self.adj.items():
            jugador = self.jugadores_map[id_j]
            resultados.append((jugador, len(vecinos)))
        return resultados
    
    
# Vértices: Cada nodo representa un objeto/diccionario Jugador.

# Aristas: Indican que dos futbolistas comparten el valor exacto del atributo filtrado seleccionado por el usuario.

# Tipo de Grafo: No Dirigido (la relación "compartir atributo con" es simétrica) y No Pesado.

# Representación: Lista de Adyacencia (dict[id_jugador] = list[vecinos]), justificado por su bajo consumo de memoria $\mathcal{O}(V + E)$ al construir dinámicamente solo la red relevante.