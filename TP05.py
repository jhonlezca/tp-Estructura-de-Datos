# Definir una jerarquía significativa del dominio, implementar el árbol general, agregar búsquedas y recorridos, e integrarlo a la interfaz de terminal (ej: opción "Explorar categorías").

# Para el TP 05 tenemos que integrar un Arbol General (o n-ario) a nuestro programa. Lo que vamos a crear para esta integracion es una funcion de busqueda de jugador por nacionalidad. Cabe aclarar que el arbol tambien nos puede permitir buscar por cualquier otro atributo de la clase jugador, pero como ejemplo tomaremos unicamente la nacionalidad. 

# La jerarquía será: 
#   Jugadores
#    |
#    |---  Nacionalidades
#    |      |
#    |      |--- Argentina
#    |      |      |--- Jug 1
#    |      |      |--- Jug 2
#    |      |--- Brasil
#    |      |    |--- ETC
#    |      |--- Uruguay
#    |      |--- ETC
#    |---  Etc

import Liga

class NodoNario:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)
        
class ArbolNacionalidades:
    def __init__(self):
        self.raiz = NodoNario("Jugadores")
        
    def cargar_jugadores_desde_equipos(self, lista_equipos):
        """ Recorre todos los equipos y sus planteles para clasificar cada jugador segun su nacionalidad"""
        lista_equipos = Liga.equiposArgentinos
        for equipo in lista_equipos:
            for jugador in equipo.plantel:
                nac = jugador.nacionalidad.strip().capitalize()
                
                # 1. Busca si el nodo de la nacionalidad ya existe entre los hijos de la raiz
                nodo_nac = self._buscar_hijo_directo(self.raiz, nac)
                
                #2. Si no existe, crea el nodo con la nacionalidad y lo agrega a la raiz
                if nodo_nac is None:
                    nodo_nac = NodoNario(nac)
                    self.raiz.agregar_hijo(nodo_nac)
                    
                # 3. Agrega al jugador como hoja del nodo de su nacionalidad
                nodo_nac.agregar_hijo(nodo_nac)
                
    def _buscar_hijo_directo(self, nodo_padre, nombre):
        """Busca entre los hijos directos de un nodo si existe alguno con ese nombre o dato"""
        for hijo in nodo_padre.hijos:
            if isinstance(hijo.dato, str) and hijo.dato.lower() == nombre.lower():
                return hijo
        return None
    
    def buscar_jugador_por_nacion(self, nacionalidad):
        """Busca el nodo de la nacionalidad pedida y devuelve una lista de objetos Jugador que esten relacionados con el"""
        nac_normalizada = nacionalidad.strip().lower()
        
        # Recorremos los hijos directos de la raiz (las nacionalidades)
        for nodo_nac in self.raiz.hijos:
            if str(nodo_nac).lower == nac_normalizada:
                # Retornamos los datos almacenados en los nodos hoja.
                return [hijo.dato for hijo in nodo_nac.hijos]
            
        return []
    
    def listar_jugadores_por_nacionalidad(self, nacionalidad):
        """Busca e imprime los jugadores asociados a una nacionalidad"""
        jugadores = self.buscar_jugador_por_nacion(nacionalidad)
        
        if jugadores:
            print(f"\n=== JUGADORES DE {nacionalidad.upper()} ({len(jugadores)}) ===")
            for jugador in jugadores:
                # Si jugador es un objeto Jugador:
                print(f"- {jugador.nombre_completo} ({jugador.posicion})")
        else:
            print(f"\n❌ No se encontraron jugadores para la nacionalidad '{nacionalidad}'.")