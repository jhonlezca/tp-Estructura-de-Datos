from Jugador import Jugador

class Equipo:
    def __init__(self, id_equipo, nombre, estadio, zona=None, pos_campeonato=None, partidos=None, plantel=None):
        self._id = id_equipo
        self._nombre = nombre
        self._estadio = estadio
        self._zona = zona
        self._pos_campeonato = pos_campeonato or {}
        self._partidos = partidos or {}
        self._plantel = []

        if plantel:
            for j in plantel:
                if isinstance(j, dict):       # viene del JSON
                    self._plantel.append(Jugador(**j))
                elif isinstance(j, Jugador):  # ya instanciado
                    self._plantel.append(j)
                else:
                    raise TypeError("El plantel debe contener diccionarios o objetos Jugador") 

# muestra la información del equipo, incluyendo su ID, nombre, estadio y zona
    def mostrar_Informacion(self):
        print(f"ID: {self._id}")
        print(f"Nombre: {self._nombre}")
        print(f"Estadio: {self._estadio}")
        print(f"Zona: {self._zona}") 

# muestra el plantel del equipo, es decir, la lista de jugadores que pertenecen al equipo

    def mostrar_Plantel(self):
        if self._plantel:
            print(f"Plantel del equipo {self._nombre}:")
            for jugador in self._plantel:
                print(jugador)
        else:
            print(f"No hay jugadores registrados en el plantel del equipo {self._nombre}.")

# agrega un jugador al plantel del equipo, añadiéndolo a la lista de jugadores

    def agregar_jugador(self, jugador):
        self._plantel.append(jugador)

# filtra los jugadores del plantel por posición, devolviendo una lista de jugadores que coinciden con la posición especificada

    def filtrar_jugadores_por_posicion(self, posicion):

        jugadores_filtrados = [jugador for jugador in self._plantel if jugador.posicion.lower() == posicion.lower()]
        return jugadores_filtrados

# filtra los jugadores del plantel por nacionalidad, mostrando la información de los jugadores que coinciden con la nacionalidad especificada en caso contrario imprime un mensaje indicando que no se encontraron jugadores con esa nacionalidad

    def filtrarJugadoresPorNacionalidad(self, nacionalidad):

        print("#### Jugadores ####")
        for jugador in self._plantel:
               if jugador.nacionalidad.lower() == nacionalidad.lower():
                   
                 
                   print(jugador)
        
        

#Prueba de la clase Equipo y la filtración de jugadores por posición


#joni = Jugador(1, "Jonathan", "Gonzalez", 10, "delantero", "argentina")
#david = Jugador(2, "David", "Martinez", 5, "defensor", "brasil")


#boca = Equipo(1, "Boca Juniors", "La Bombonera", "Zona A", {"posicion": 1}, {"partidos": 10}, [joni, david])
#boca.filtrarJugadoresPorNacionalidad("brasil")
