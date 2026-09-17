class Jugador:
    def __init__(self, id_jugador, id_equipo, nombre, apellido, dorsal, posicion):
        self.id_jugador = id_jugador
        self.id_equipo = id_equipo
        self.nombre = nombre
        self.apellido = apellido
        self.dorsal = dorsal
        self.posicion = posicion
    
    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}".strip()
    
    @property
    def dorsal(self):
        return self._dorsal
    
    @property
    def posicion(self):
        return self._posicion
    
    def __str__(self):
        return f"{self.dorsal}, {self.nombre} {self.apellido}, {self.posicion}"
    
    def __repr__(self):
        return f"Jugador(id={self._id_jugador!r}, nombre={self._nombre!r}, dorsal={self._dorsal!r})"
    
    
class Equipo:
    def __init__(self, id_equipo, nombre, estadio, zona=None, pos_campeonato=None, partidos=None):
        self._id = id_equipo
        self._nombre = nombre
        self._estadio = estadio
        self._zona = zona
        self._pos_campeonato = pos_campeonato or {}
        self._partidos = partidos or {}
        self._plantel = []
        
    @property
    def id(self):
        return self._id
    @property
    def nombre(self):
        return self._nombre
    @property
    def estadio(self):
        return self._estadio
    @property
    def zona(self):
        return self._zona
    @property
    def partidos(self):
        return self._partidos
    @property
    def plantel(self):
        return self._plantel
    
    
    def __repr__(self):
        return f"Equipo (id={self._id!r})"